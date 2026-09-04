"""Independent exact-rule checks. No model calls or application-gate imports."""
from datetime import date
from bank_review.validation import structure_errors


def verdict(failures, missing):
    if failures:
        return {"status": "fail", "reason": "; ".join(failures)}
    if missing:
        return {"status": "unknown", "reason": "; ".join(missing)}
    return {"status": "pass", "reason": "All inspectable exact checks passed; semantic support still requires review."}


def evidence_reference_integrity(input, output):
    failures, missing = [], []
    errors = structure_errors(input, output)
    if errors:
        return verdict([e for e in errors if "Duplicate" in e], errors)
    if not isinstance(output, dict) or not isinstance(input, dict):
        return verdict([], ["Input or output unavailable"])
    findings, docs, profile = output.get("findings"), input.get("evidence"), input.get("profile")
    if not isinstance(findings, list) or not findings or not isinstance(docs, list) or not isinstance(profile, dict):
        return verdict([], ["Findings, source packet or profile unavailable"])
    by_id = {d.get("id"): d for d in docs}
    for f in findings:
        if not isinstance(f, dict) or not isinstance(f.get("citations"), list):
            missing.append("Finding citation fields absent")
            continue
        if not f["citations"] and f.get("evidence_status") not in ("missing", "retrieval_error"):
            failures.append(f"{f.get('requirement_id')}: supported claim without citations")
        for citation in f["citations"]:
            if not isinstance(citation, dict) or not all(citation.get(k) for k in ("evidence_id", "passage_id", "quote")):
                missing.append("Citation identifier or quote absent")
                continue
            doc = by_id.get(citation["evidence_id"])
            if doc is None:
                failures.append("Citation references a nonexistent source")
                continue
            for key, target in (("vendor_id", "vendor_id"), ("use_case_id", "profile_id")):
                if not profile.get(target) or not doc.get(key):
                    missing.append(f"Missing {key} binding")
                elif doc[key] != profile[target]:
                    failures.append(f"Citation has wrong {key}")
            if "retrieval_status" not in doc or "passages" not in doc:
                missing.append("Source retrieval evidence absent")
                continue
            if doc["retrieval_status"] != "available":
                failures.append("Citation uses unavailable source content")
            passage = next((p for p in doc["passages"] if p.get("id") == citation["passage_id"]), None)
            if not passage or citation["quote"] not in passage.get("text", ""):
                failures.append("Citation passage or exact quote does not exist")
    return verdict(failures, missing)


def evidence_status_and_routing(input, output):
    failures, missing = [], []
    errors = structure_errors(input, output)
    if errors:
        return verdict([e for e in errors if "Duplicate" in e], errors)
    if not isinstance(input, dict) or not isinstance(output, dict):
        return verdict([], ["Input or output unavailable"])
    docs, profile, findings = input.get("evidence"), input.get("profile"), output.get("findings")
    if not isinstance(docs, list) or not isinstance(profile, dict) or not isinstance(findings, list) or not findings:
        return verdict([], ["Source packet, profile or findings unavailable"])
    for key, value in (("human_review_required", True), ("pilot_approved", False)):
        if key not in output:
            missing.append(f"{key} absent")
        elif output[key] is not value:
            failures.append(f"{key} violates prototype authority")
    state = output.get("packet_status")
    if state is None:
        missing.append("Packet status absent")
    elif state not in ("ready_for_human_review", "needs_evidence", "withheld"):
        failures.append("Invalid packet status")
    if not isinstance(output.get("scope"), list) or not output["scope"]:
        missing.append("Scope unavailable")
    elif any(s.get("applicability") == "needs_clarification" for s in output["scope"]) and state == "ready_for_human_review":
        failures.append("Unresolved scope marked ready")
    by_id = {d.get("id"): d for d in docs}
    # Independent scope rule: unknown intended use cannot become an exclusion.
    for item in output.get("scope", []):
        field = {"SEC-01": "restricted_documents", "FAIR-02": "credit_decisions"}.get(item.get("requirement_id"))
        if field and field in profile:
            value = profile[field]
            expected = "needs_clarification" if value is None else ("applicable" if value is True else "not_applicable")
            if item.get("applicability") != expected:
                failures.append(f"{item.get('requirement_id')}: scope contradicts intended-use field")
    for f in findings:
        status = f.get("evidence_status")
        if status is None:
            missing.append("Finding status absent")
        if status in ("missing", "retrieval_error", "conflicting") and state == "ready_for_human_review":
            failures.append("Unresolved evidence marked ready")
        if status != "tested_in_scope":
            continue
        citations = f.get("citations")
        if not isinstance(citations, list):
            missing.append("Test claim citations absent")
            continue
        matched = []
        for c in citations:
            d = by_id.get(c.get("evidence_id"))
            if d and d.get("evidence_type") == "observed_test_result":
                matched.append(d)
        if not matched:
            failures.append("Tested claim lacks a supplied test record")
        for d in matched:
            for key, target in (("vendor_id", "vendor_id"), ("use_case_id", "profile_id"), ("system_version", "system_version")):
                if not d.get(key) or not profile.get(target):
                    missing.append(f"Test {key} evidence absent")
                elif d[key] != profile[target]:
                    failures.append(f"Test {key} mismatch")
            if "requirement_ids" not in d:
                missing.append("Test requirement binding absent")
            elif f.get("requirement_id") not in d["requirement_ids"]:
                failures.append("Test does not cover finding requirement")
            for key in ("method", "limitations"):
                if not d.get(key):
                    missing.append(f"Test {key} absent")
            for key, expected in (("retrieval_status", "available"), ("result", "pass")):
                if key not in d:
                    missing.append(f"Test {key} absent")
                elif d[key] != expected:
                    failures.append(f"Test {key} is not {expected}")
            try:
                dates = [input.get("assessment_date"), d.get("issued_on"), d.get("valid_through")]
                if not all(dates):
                    missing.append("Test date evidence absent")
                else:
                    assessed, issued, valid = map(date.fromisoformat, dates)
                    if not issued <= assessed <= valid:
                        failures.append("Test outside validity window")
            except (ValueError, TypeError):
                failures.append("Malformed test dates")
    return verdict(failures, missing)
