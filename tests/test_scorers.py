import copy
import unittest
from bank_review.scorers import evidence_reference_integrity, evidence_status_and_routing


class ScorerTests(unittest.TestCase):
    def setUp(self):
        # Independent calibration fixture, not derived from the application output.
        self.input = {"assessment_date": "2026-09-04", "profile": {
            "vendor_id": "VENDOR-001", "profile_id": "UC-001", "system_version": "v1"},
            "evidence": [{"id": "T1", "vendor_id": "VENDOR-001", "use_case_id": "UC-001",
                "system_version": "v1", "evidence_type": "observed_test_result",
                "requirement_ids": ["SEC-01"], "retrieval_status": "available",
                "issued_on": "2026-09-01", "valid_through": "2026-10-01",
                "method": "Query two roles", "result": "pass", "limitations": "Two roles only",
                "passages": [{"id": "p1", "text": "Two roles isolated in this synthetic test."}]}]}
        self.output = {"scope": [{"requirement_id": "SEC-01", "applicability": "applicable"}],
            "findings": [{"requirement_id": "SEC-01", "evidence_status": "tested_in_scope",
                "citations": [{"evidence_id": "T1", "passage_id": "p1", "quote": "Two roles isolated"}]}],
            "packet_status": "ready_for_human_review", "human_review_required": True, "pilot_approved": False}

    def test_reference_pass(self):
        self.assertEqual(evidence_reference_integrity(self.input, self.output)["status"], "pass")

    def test_reference_wrong_vendor_fail(self):
        self.input["evidence"][0]["vendor_id"] = "OTHER"
        self.assertEqual(evidence_reference_integrity(self.input, self.output)["status"], "fail")

    def test_reference_unknown(self):
        del self.input["evidence"]
        self.assertEqual(evidence_reference_integrity(self.input, self.output)["status"], "unknown")

    def test_status_pass(self):
        self.assertEqual(evidence_status_and_routing(self.input, self.output)["status"], "pass")

    def test_assertion_cannot_be_test(self):
        self.input["evidence"][0]["evidence_type"] = "vendor_assertion"
        self.assertEqual(evidence_status_and_routing(self.input, self.output)["status"], "fail")

    def test_status_unknown(self):
        del self.input["evidence"][0]["method"]
        self.assertEqual(evidence_status_and_routing(self.input, self.output)["status"], "unknown")

    def test_stale_and_wrong_version(self):
        for key, value in (("valid_through", "2026-09-01"), ("system_version", "old")):
            with self.subTest(key=key):
                packet = copy.deepcopy(self.input)
                packet["evidence"][0][key] = value
                self.assertEqual(evidence_status_and_routing(packet, self.output)["status"], "fail")

    def test_honest_missing_evidence_passes(self):
        self.output["findings"][0].update(evidence_status="missing", citations=[])
        self.output["packet_status"] = "needs_evidence"
        self.assertEqual(evidence_reference_integrity(self.input, self.output)["status"], "pass")
        self.assertEqual(evidence_status_and_routing(self.input, self.output)["status"], "pass")

    def test_timeout_cannot_be_test(self):
        self.input["evidence"][0].update(retrieval_status="error", result=None, passages=[])
        self.assertEqual(evidence_reference_integrity(self.input, self.output)["status"], "fail")
        self.assertEqual(evidence_status_and_routing(self.input, self.output)["status"], "fail")

    def test_missing_fields_cannot_pass(self):
        self.assertEqual(evidence_status_and_routing(self.input, {})["status"], "unknown")


if __name__ == "__main__":
    unittest.main()
