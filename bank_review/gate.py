"""V2 post-generation evidence gate, independent of evaluation scorers."""
from copy import deepcopy
from datetime import date
import weave


@weave.op()
def apply_evidence_gate(input: dict, draft: dict) -> dict:
    output = deepcopy(draft)
    records = {record["id"]: record for record in input["evidence"]}
    profile = input["profile"]
    rejected = []
    for finding in draft["findings"]:
        if finding["evidence_status"] != "tested_in_scope":
            continue
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
        if qualifying_tests == 0:
            reasons.append("no supplied behavioral test")
        if reasons:
            rejected.append({"requirement_id": finding["requirement_id"], "reasons": sorted(set(reasons))})
    if rejected:
        # Withhold the whole generated narrative so an unsafe claim cannot survive
        # in another finding, rationale or question. Original draft stays in trace.
        output["scope"] = [{**s, "rationale": "Generated assessment withheld pending evidence validation."} for s in draft["scope"]]
        output["findings"] = [{"requirement_id": r["requirement_id"],
                               "claim": "Behavioral verification could not be established from eligible supplied evidence; original assessment withheld.",
                               "evidence_status": "missing", "citations": []} for r in rejected]
        output["questions"] = [{"requirement_id": r["requirement_id"],
                                "question": "Supply a current, matching behavioral test with method, passing result and limitations. Validation gaps: " + "; ".join(r["reasons"]),
                                "owner": "bank_security"} for r in rejected]
        output.update(packet_status="withheld", human_review_required=True, pilot_approved=False)
    output["gate_record"] = {"applied": True, "reason": "Evidence gate v1.0", "rejected": rejected}
    return output
