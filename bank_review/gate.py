"""V2 post-generation evidence gate, independent of evaluation scorers."""
from copy import deepcopy
from datetime import date
import weave
from bank_review.validation import structure_errors


@weave.op()
def apply_evidence_gate(input: dict, draft: dict) -> dict:
    errors = structure_errors(input, draft)
    if errors:
        return {"scope": [], "findings": [], "questions": [], "packet_status": "withheld",
                "human_review_required": True, "pilot_approved": False, "execution_error": "InvalidStructure",
                "gate_record": {"applied": True, "reason": "Validation gate v2.0", "rejected": [], "errors": errors}}
    output = deepcopy(draft)
    records = {record["id"]: record for record in input["evidence"]}
    profile = input["profile"]
    rejected = []
    scope_rejected = []
    for scope in output["scope"]:
        field = {"SEC-01": "restricted_documents", "FAIR-02": "credit_decisions"}.get(scope.get("requirement_id"))
        if field and field in profile:
            value = profile[field]
            expected = "needs_clarification" if value is None else ("applicable" if value is True else "not_applicable")
            if scope.get("applicability") != expected:
                scope["applicability"] = expected
                scope_rejected.append({"requirement_id": scope["requirement_id"], "reasons": [f"Clarify intended use: {field}; original scope decision was unsupported"]})
    for finding in draft["findings"]:
        reasons, qualifying_tests = [], 0
        for citation in finding["citations"]:
            record = records.get(citation["evidence_id"])
            if record is None:
                reasons.append("cited source is absent")
                continue
            if record.get("vendor_id") != profile["vendor_id"] or record.get("use_case_id") != profile["profile_id"]:
                reasons.append("source identity mismatch")
            if record.get("retrieval_status") != "available":
                reasons.append("source retrieval is unavailable")
            passages = {p["id"]: p["text"] for p in record.get("passages", [])}
            if not citation["quote"] or citation["quote"] not in passages.get(citation["passage_id"], ""):
                reasons.append("quoted passage is unavailable")
            if finding["requirement_id"] not in record.get("requirement_ids", []):
                reasons.append("source requirement mismatch")
            if finding["evidence_status"] != "tested_in_scope":
                continue
            if record.get("evidence_type") != "observed_test_result":
                continue
            qualifying_tests += 1
            if record.get("system_version") != profile["system_version"]:
                reasons.append("test version mismatch")
            if finding["requirement_id"] not in record.get("requirement_ids", []):
                reasons.append("test requirement mismatch")
            if record.get("result") != "pass":
                reasons.append("no passing test result")
            if not record.get("method") or not record.get("limitations"):
                reasons.append("test method or limitations missing")
            try:
                assessed = date.fromisoformat(input["assessment_date"])
                if not date.fromisoformat(record["issued_on"]) <= assessed <= date.fromisoformat(record["valid_through"]):
                    reasons.append("test outside review window")
            except (KeyError, ValueError, TypeError):
                reasons.append("test dates unavailable")
        if finding["evidence_status"] == "tested_in_scope" and qualifying_tests == 0:
            reasons.append("no supplied behavioral test")
        if reasons:
            rejected.append({"requirement_id": finding["requirement_id"], "reasons": sorted(set(reasons))})
    rejected.extend(scope_rejected)
    if rejected:
        # Withhold the whole generated narrative so an unsafe claim cannot survive
        # in another finding, rationale or question. Original draft stays in trace.
        output["scope"] = [{**s, "rationale": "Generated assessment withheld pending evidence and scope validation."} for s in output["scope"]]
        output["findings"] = [{"requirement_id": r["requirement_id"],
                               "claim": "Behavioral verification could not be established from eligible supplied evidence; original assessment withheld.",
                               "evidence_status": "missing", "citations": []} for r in rejected]
        output["questions"] = [{"requirement_id": r["requirement_id"],
                                "question": ("Clarify the bank's intended use. " if r in scope_rejected else "Supply a current, matching behavioral test with method, passing result and limitations. ") + "Validation gaps: " + "; ".join(r["reasons"]),
                                "owner": "bank_security"} for r in rejected]
        output.update(packet_status="withheld", human_review_required=True, pilot_approved=False)
    output["gate_record"] = {"applied": True, "reason": "Evidence and scope validation gate v2.0", "rejected": rejected}
    return output
