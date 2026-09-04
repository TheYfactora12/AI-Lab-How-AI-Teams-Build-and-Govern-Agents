"""Run the frozen five-case comparison with native Weave evaluations."""
import asyncio
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import weave
from bank_review.app import VendorReviewer, MODEL, PROJECT
from bank_review.judge import BankRiskJudge, final_verdict
from bank_review.publish import score_references, score_status

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evaluation_output"


class RecordedEvaluation(weave.Evaluation):
    """Preserve row-level results without rerunning any model calls."""

    async def get_eval_results(self, model):
        results = await super().get_eval_results(model)
        rows = list(results.rows)
        inputs = list(self.dataset.rows)
        recorded = [{"case_id": case["case_id"], **row} for case, row in zip(inputs, rows, strict=True)]
        for row in recorded:
            row["final_verdict"] = final_verdict(row.get("scores", {}))
        (OUTPUT / f"{model.application_version}-rows.json").write_text(json.dumps(recorded, indent=2), encoding="utf-8")
        return results


async def main():
    contract = json.loads((ROOT / "evaluation_contract.json").read_text())
    for filename, digest in contract["file_hashes"].items():
        if hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Frozen contract changed: {filename}. Freeze a new contract before rerunning both versions.")
    OUTPUT.mkdir(exist_ok=True)
    catalog = json.loads((ROOT / "data/assessment_catalog.json").read_text())
    client = weave.init(PROJECT)
    dataset = weave.ref(contract["dataset_uri"]).get()
    rows = list(dataset.rows)
    local_cases = [json.loads(line) for line in (ROOT / "data/cases.jsonl").read_text().splitlines()]
    local_expected = json.loads((ROOT / "data/expected_findings.json").read_text())
    if len(rows) != 5:
        raise ValueError("Expected exactly five remote cases")
    for remote, case, expected in zip(rows, local_cases, local_expected, strict=True):
        if remote["case_id"] != case["case_id"] or remote["input"] != case["input"] or remote["expected"] != expected:
            raise ValueError("Remote dataset differs from frozen local inputs/expectations")
    judge = BankRiskJudge(name="BankRiskJudge", rubric=(ROOT / "JUDGE_RUBRIC.md").read_text(), catalog=catalog)
    evaluation = RecordedEvaluation(name="bank-vendor-controlled-evaluation",
                                    dataset=dataset, scorers=[score_references, score_status, judge],
                                    trials=1, metadata=contract)
    receipt = {"contract": contract, "git_commit": os.environ.get("GITHUB_SHA"),
               "workflow_run": os.environ.get("GITHUB_RUN_ID"), "runs": {},
               "notice": "Actual model evaluations of an assessor on synthetic cases; not real vendor validation."}
    try:
        for version in ("v1", "v2"):
            model = VendorReviewer(application_version=version, catalog=catalog)
            with weave.attributes({"contract_id": contract["contract_id"], "application_version": version,
                                   "changed_dimension": "post_generation_evidence_gate"}):
                summary, call = await evaluation.evaluate.call(evaluation, model=model)
            client.flush()
            stored = client.get_call(call.id)
            if call.exception or stored.exception or stored.output != summary:
                raise RuntimeError(f"{version} evaluation/readback failed")
            receipt["runs"][version] = {"trace_url": f"https://wandb.ai/{PROJECT}/weave/calls/{call.id}",
                                        "call_id": call.id, "summary": summary}
            (OUTPUT / "receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        lines = ["# Controlled evaluation results", f"Contract: {contract['contract_id']}",
                 "| Case | V1 final | V2 final | V2 gate rejected |", "| --- | --- | --- | --- |"]
        version_rows = {v: json.loads((OUTPUT / f"{v}-rows.json").read_text()) for v in ("v1", "v2")}
        errors = []
        for a, b in zip(version_rows["v1"], version_rows["v2"], strict=True):
            lines.append(f"| {a['case_id']} | {a['final_verdict']} | {b['final_verdict']} | {len((b.get('output') or {}).get('gate_record', {}).get('rejected', []))} |")
        for version, evaluated in version_rows.items():
            lines += [f"[{version} evaluation]({receipt['runs'][version]['trace_url']})",
                      f"{version} final verdict counts: {dict(Counter(r['final_verdict'] for r in evaluated))}"]
            for row in evaluated:
                scores = row.get("scores", {})
                if not row.get("output") or not all(scores.get(k) for k in ("score_references", "score_status", "BankRiskJudge")) or scores.get("BankRiskJudge", {}).get("error"):
                    errors.append(f"{version}/{row['case_id']}: incomplete model or scoring result")
        lines += ["All findings remain drafts for human review. A block is an assessment-quality decision, not a legal/vendor conclusion."]
        if errors:
            lines += errors
        receipt["complete"] = not errors
        receipt["errors"] = errors
        (OUTPUT / "receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        (OUTPUT / "SUMMARY.md").write_text("\n\n".join(lines), encoding="utf-8")
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
                f.write("\n\n".join(lines))
        if errors:
            raise RuntimeError("Evaluation infrastructure incomplete; see saved errors")
    finally:
        (OUTPUT / "receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        weave.finish()


if __name__ == "__main__":
    asyncio.run(main())
