import copy
import unittest
from unittest.mock import patch
from pydantic import ValidationError
from bank_review.app import VendorReviewer
from bank_review.schema import Assessment
from bank_review.gate import apply_evidence_gate
from bank_review.judge import criterion_verdict, final_verdict
import test_scorers


class GateTests(unittest.TestCase):
    def setUp(self):
        fixture = test_scorers.ScorerTests()
        fixture.setUp()
        self.input = fixture.input
        self.draft = fixture.output
        self.draft["scope"][0]["rationale"] = "A scoped role test is relevant."
        self.draft["findings"][0]["claim"] = "Role isolation tested under two roles."
        self.draft["questions"] = []

    def test_preserves_eligible_draft(self):
        original = copy.deepcopy(self.draft)
        result = apply_evidence_gate(self.input, self.draft)
        self.assertEqual(result["findings"], original["findings"])
        self.assertEqual(result["gate_record"]["rejected"], [])
        self.assertEqual(self.draft, original)

    def test_assertion_withholds_narrative(self):
        self.input["evidence"][0]["evidence_type"] = "vendor_assertion"
        self.draft["questions"] = [{"question": "Unsafe guarantee elsewhere"}]
        result = apply_evidence_gate(self.input, self.draft)
        self.assertEqual(result["packet_status"], "withheld")
        self.assertNotIn("Role isolation tested under two roles", str(result))
        self.assertNotIn("Unsafe guarantee elsewhere", str(result))
        self.assertTrue(result["human_review_required"])

    def test_invalid_evidence_is_withheld(self):
        for field, bad in [("vendor_id", "OTHER"), ("system_version", "old"), ("valid_through", "2026-01-01"),
                           ("method", None), ("retrieval_status", "error"), ("result", "fail")]:
            packet = copy.deepcopy(self.input)
            packet["evidence"][0][field] = bad
            with self.subTest(field=field):
                self.assertEqual(apply_evidence_gate(packet, self.draft)["packet_status"], "withheld")

    def test_documentary_claim_not_rewritten(self):
        self.draft["findings"][0]["evidence_status"] = "documented"
        result = apply_evidence_gate(self.input, self.draft)
        self.assertEqual(result["findings"], self.draft["findings"])


class JudgePolicyTests(unittest.TestCase):
    def test_invalid_generation_is_explicit_for_both_versions(self):
        fixture = test_scorers.ScorerTests()
        fixture.setUp()
        try:
            Assessment.model_validate({})
        except ValidationError as exc:
            error = exc
        for version in ("v1", "v2"):
            with patch("bank_review.app.generate_assessment", side_effect=error):
                result = VendorReviewer(application_version=version, catalog={}).predict(fixture.input)
            self.assertEqual(result["execution_error"], "ValidationError")
            self.assertEqual(result["packet_status"], "withheld")
            self.assertEqual(result["findings"], [])
            self.assertFalse(result["gate_record"]["applied"])

    def test_all_verdict_branches(self):
        data = {k: {"status": "pass"} for k in ("evidence_support", "scope_and_risk", "follow_up_quality")}
        self.assertEqual(criterion_verdict(data), "pass")
        data["follow_up_quality"]["status"] = "fail"
        self.assertEqual(criterion_verdict(data), "review")
        data["evidence_support"]["status"] = "unknown"
        self.assertEqual(criterion_verdict(data), "review")
        data["scope_and_risk"]["status"] = "fail"
        self.assertEqual(criterion_verdict(data), "block")

    def test_exact_fail_cannot_be_overridden(self):
        scores = {"score_references": {"status": "fail"}, "score_status": {"status": "pass"}, "BankRiskJudge": {"verdict": "pass"}}
        self.assertEqual(final_verdict(scores), "block")
        self.assertEqual(final_verdict({}), "review")
