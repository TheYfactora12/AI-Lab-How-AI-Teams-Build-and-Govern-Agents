"""Explicitly freeze current sources; run before, never inside, comparison workflow."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ["data/assessment_catalog.json", "data/cases.jsonl", "data/expected_findings.json",
         "bank_review/app.py", "bank_review/schema.py", "bank_review/gate.py", "bank_review/scorers.py",
         "bank_review/judge.py", "bank_review/validation.py", "bank_review/publish.py", "bank_review/evaluate.py", "JUDGE_RUBRIC.md", "requirements.txt"]
contract = {
    "contract_id": "bank-vendor-eval-v1.3",
    "dataset_uri": "weave:///kevinmedeiros-masterclass/ai-lab-agent-governance/object/bank-vendor-scope-five-v1:Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs",
    "catalog_id": "bank-ai-scope-v1.0", "scorer_set": "exact-rules-v1.1", "rubric_id": "bank-risk-judge-v1.2",
    "release_policy": "exact-fail-or-blocking-judge-fail-block; unknown-review; all-pass-human-review-only-v1.0",
    "app_model": "OpenPipe/Qwen3-14B-Instruct", "judge_model": "OpenPipe/Qwen3-14B-Instruct",
    "temperature": 0, "trials_per_case": 1, "app_max_tokens": 6000, "judge_max_tokens": 3000,
    "automatic_retries": 0, "planned_hosted_calls": 20,
    "only_changed_dimension": "post_generation_evidence_gate",
    "answer_key_provenance": "AI-assisted pre-run design; no independent expert validation claimed",
    "file_hashes": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in FILES},
}
(ROOT / "evaluation_contract.json").write_text(json.dumps(contract, indent=2)+"\n", encoding="utf-8", newline="\n")
print("Frozen", contract["contract_id"])
