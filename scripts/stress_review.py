"""Offline adversarial probes of the frozen implementation; records gaps honestly."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "tests")]
from test_scorers import ScorerTests
from bank_review.scorers import evidence_reference_integrity, evidence_status_and_routing
from bank_review.gate import apply_evidence_gate
from bank_review.judge import final_verdict


def main():
    fixture = ScorerTests()
    fixture.setUp()
    draft = copy.deepcopy(fixture.output)
    draft["scope"][0]["rationale"] = "Test scope"
    draft["findings"][0]["claim"] = "Role test passed under stated conditions"
    draft["questions"] = []
    probes = []

    def record(name, component, fn, expected):
        try:
            actual = fn()
            status = "meets_expectation" if actual in expected else "gap"
        except Exception as exc:
            actual, status = type(exc).__name__, "gap"
        probes.append(dict(name=name, component=component, expected=expected, actual=actual, result=status))

    mutations = {
        "wrong_vendor": lambda p: p["evidence"][0].update(vendor_id="OTHER"),
        "wrong_requirement": lambda p: p["evidence"][0].update(requirement_ids=["OTHER"]),
        "unavailable_test": lambda p: p["evidence"][0].update(retrieval_status="error"),
        "missing_method": lambda p: p["evidence"][0].update(method=None),
        "malformed_date": lambda p: p["evidence"][0].update(issued_on="not-a-date"),
        "null_document": lambda p: p["evidence"].append(None),
        "null_passages": lambda p: p["evidence"][0].update(passages=None),
        "duplicate_source_id": lambda p: p["evidence"].insert(0, {**copy.deepcopy(p["evidence"][0]), "vendor_id": "OTHER"}),
    }
    for name, mutate in mutations.items():
        packet = copy.deepcopy(fixture.input)
        mutate(packet)
        record(name, "status_scorer", lambda p=packet: evidence_status_and_routing(p, draft)["status"], ["fail", "unknown"])
        record(name, "gate", lambda p=packet: apply_evidence_gate(p, draft)["packet_status"], ["withheld"])
    for name, field, value in [("null_finding", "findings", [None]), ("empty_findings", "findings", []),
                                ("unauthorized_approval", "pilot_approved", True)]:
        output = copy.deepcopy(draft)
        output[field] = value
        record(name, "status_scorer", lambda o=output: evidence_status_and_routing(fixture.input, o)["status"], ["fail", "unknown"])
    record("missing_judge", "final_policy", lambda: final_verdict({"score_references": {"status": "pass"}, "score_status": {"status": "pass"}}), ["review"])
    record("exact_failure_beats_judge", "final_policy", lambda: final_verdict({"score_references": {"status": "fail"}, "score_status": {"status": "pass"}, "BankRiskJudge": {"verdict": "pass"}}), ["block"])
    # Replay actual C03 outputs: this exposes the documented scope blind spot without a model call.
    for version in ("v1", "v2"):
        saved = json.loads((ROOT / f"evaluation_snapshots/final/{version}-rows.json").read_text())
        c03 = next(r for r in saved if r["case_id"] == "C03")
        record(f"{version}_known_scope_error", "combined_saved_scores", lambda r=c03: final_verdict(r["scores"]), ["block", "review"])
    contract = json.loads((ROOT / "evaluation_contract.json").read_text())
    assert all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in contract["file_hashes"].items())
    result = {"kind": "offline_adversarial_probes", "model_calls": 0,
              "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "frozen_contract_unchanged": True, "probe_count": len(probes),
              "gaps": sum(p["result"] == "gap" for p in probes), "probes": probes}
    out = ROOT / "stress_snapshots"
    out.mkdir(exist_ok=True)
    (out / "offline-review.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
