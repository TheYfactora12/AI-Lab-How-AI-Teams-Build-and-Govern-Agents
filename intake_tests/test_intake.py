import unittest
from bank_review.intake import validate_record


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.record = dict(document_id="D1", vendor_id="A", sha256="abc", url="https://example.com/report",
                           format="pdf", retrieved_at="2026-09-04", byte_count=100, text_character_count=50)
        self.expected = dict(self.record)

    def test_valid_metadata_never_authorizes_assessment(self):
        result = validate_record(self.record, self.expected, "A")
        self.assertEqual(result["status"], "pass")
        self.assertFalse(result["assessment_permission"])

    def test_cross_vendor(self):
        self.assertIn("vendor_mismatch", validate_record(self.record, self.expected, "B")["reasons"])

    def test_changed_file_same_url(self):
        self.record["sha256"] = "changed"
        self.assertIn("sha256_mismatch", validate_record(self.record, self.expected, "A")["reasons"])

    def test_duplicate(self):
        self.assertIn("duplicate_content", validate_record(self.record, self.expected, "A", ["abc"])["reasons"])

    def test_empty_extraction(self):
        self.record["text_character_count"] = 0
        self.assertIn("text_unavailable", validate_record(self.record, self.expected, "A")["reasons"])

    def test_missing_provenance(self):
        del self.record["retrieved_at"]
        self.assertIn("incomplete_provenance", validate_record(self.record, self.expected, "A")["reasons"])
