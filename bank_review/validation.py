"""Structural validation only; no grading or evidence eligibility decisions."""


def structure_errors(packet, output=None):
    errors = []
    if not isinstance(packet, dict) or not isinstance(packet.get("profile"), dict):
        return ["Packet or profile unavailable"]
    if not isinstance(packet.get("assessment_date"), str):
        errors.append("Assessment date unavailable")
    for key in ("vendor_id", "profile_id", "system_version"):
        if not isinstance(packet["profile"].get(key), str):
            errors.append(f"Profile {key} unavailable")
    for key in ("restricted_documents", "credit_decisions"):
        if key in packet["profile"] and packet["profile"][key] is not None and type(packet["profile"][key]) is not bool:
            errors.append(f"Invalid intended-use boolean: {key}")
    docs = packet.get("evidence")
    if not isinstance(docs, list):
        return ["Evidence collection unavailable"]
    seen = set()
    for doc in docs:
        if not isinstance(doc, dict) or not isinstance(doc.get("id"), str) or not doc["id"]:
            errors.append("Malformed evidence record")
            continue
        if doc["id"] in seen:
            errors.append("Duplicate evidence identifier")
        seen.add(doc["id"])
        passages = doc.get("passages")
        if not isinstance(passages, list):
            errors.append("Passages unavailable")
            continue
        ids = set()
        for p in passages:
            if not isinstance(p, dict) or not isinstance(p.get("id"), str) or not isinstance(p.get("text"), str):
                errors.append("Malformed passage")
                continue
            if p["id"] in ids:
                errors.append("Duplicate passage identifier")
            ids.add(p["id"])
        if "requirement_ids" in doc and (not isinstance(doc["requirement_ids"], list) or any(not isinstance(x, str) for x in doc["requirement_ids"])):
            errors.append("Malformed requirement binding")
    if output is not None:
        if not isinstance(output, dict):
            return errors + ["Assessment unavailable"]
        for field in ("scope", "findings"):
            if not isinstance(output.get(field), list) or any(not isinstance(x, dict) for x in output[field]):
                errors.append(f"Malformed {field}")
        for finding in output.get("findings", []) if isinstance(output.get("findings"), list) else []:
            if not isinstance(finding, dict):
                continue
            citations = finding.get("citations")
            if not isinstance(citations, list) or any(not isinstance(c, dict) or any(not isinstance(c.get(k), str) for k in ("evidence_id", "passage_id", "quote")) for c in citations):
                errors.append("Malformed citations")
    return sorted(set(errors))
