import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from bank_review.app import VendorReviewer
from bank_review.gate import apply_evidence_gate
from bank_review.judge import BankRiskJudge
from bank_review.scorers import evidence_reference_integrity, evidence_status_and_routing
import test_scorers

ROOT = Path(__file__).resolve().parents[1]


class HardeningTests(unittest.TestCase):
    def setUp(self):
        f = test_scorers.ScorerTests(); f.setUp()
        self.packet, self.draft = f.input, f.output
        self.draft["questions"] = []

    def test_malformed_packet_and_findings_never_crash_or_pass(self):
        mutations = [lambda p: p["evidence"].append(None),
                     lambda p: p["evidence"][0].update(passages=None)]
        for mutate in mutations:
            packet = copy.deepcopy(self.packet); mutate(packet)
            for scorer in (evidence_reference_integrity, evidence_status_and_routing):
                self.assertEqual(scorer(packet, self.draft)["status"], "unknown")
            self.assertEqual(apply_evidence_gate(packet, self.draft)["packet_status"], "withheld")
        self.draft["findings"] = [None]
        self.assertEqual(evidence_status_and_routing(self.packet, self.draft)["status"], "unknown")
        self.assertEqual(apply_evidence_gate(self.packet, self.draft)["packet_status"], "withheld")

    def test_duplicate_source_rejected_in_either_order(self):
        other = {**copy.deepcopy(self.packet["evidence"][0]), "vendor_id": "OTHER"}
        for docs in ([other, self.packet["evidence"][0]], [self.packet["evidence"][0], other]):
            packet = {**self.packet, "evidence": docs}
            self.assertEqual(evidence_reference_integrity(packet, self.draft)["status"], "fail")
            self.assertEqual(evidence_status_and_routing(packet, self.draft)["status"], "fail")
            self.assertEqual(apply_evidence_gate(packet, self.draft)["packet_status"], "withheld")

    def test_invalid_packet_stops_before_model_for_both_versions(self):
        self.packet["evidence"] = [None]
        with patch("bank_review.app.generate_assessment") as model:
            for version in ("v1", "v2"):
                result = VendorReviewer(application_version=version, catalog={}).predict(self.packet)
                self.assertEqual(result["packet_status"], "withheld")
            model.assert_not_called()

    def test_error_envelope_never_invokes_judge(self):
        with patch("bank_review.judge.OpenAI") as client:
            result = BankRiskJudge(rubric="test", catalog={}).score({}, {}, {"execution_error": "ValidationError"})
            client.assert_not_called()
        self.assertEqual(result["verdict"], "review")
        self.assertTrue(all(result[k]["status"] == "unknown" for k in ("evidence_support", "scope_and_risk", "follow_up_quality")))

    def test_actual_c03_failure_is_detected_and_withheld(self):
        packet = next(json.loads(x)["input"] for x in (ROOT / "data/cases.jsonl").read_text().splitlines() if json.loads(x)["case_id"] == "C03")
        for version in ("v1", "v2"):
            draft = next(r["output"] for r in json.loads((ROOT / f"evaluation_snapshots/final/{version}-rows.json").read_text()) if r["case_id"] == "C03")
            self.assertEqual(evidence_status_and_routing(packet, draft)["status"], "fail")
            result = apply_evidence_gate(packet, draft)
            self.assertEqual(result["packet_status"], "withheld")
            for scope in result["scope"]:
                if scope["requirement_id"] in ("SEC-01", "FAIR-02"):
                    self.assertEqual(scope["applicability"], "needs_clarification")
            self.assertEqual(evidence_status_and_routing(packet, result)["status"], "pass")
