"""Publish review data and optionally generate one real V1 review sample."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import weave
from bank_review.app import PROJECT, VendorReviewer
from bank_review.scorers import evidence_reference_integrity, evidence_status_and_routing

ROOT = Path(__file__).resolve().parents[1]


@weave.op()
def score_references(input: dict, output: dict) -> dict:
    return evidence_reference_integrity(input, output)


@weave.op()
def score_status(input: dict, output: dict) -> dict:
    return evidence_status_and_routing(input, output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()
    data = ROOT / "data"
    manifest = json.loads((data / "manifest.json").read_text())
    for name, digest in manifest["files"].items():
        if hashlib.sha256((data / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Dataset fingerprint mismatch: {name}")
    cases = [json.loads(line) for line in (data / "cases.jsonl").read_text().splitlines()]
    expected = {row["case_id"]: row for row in json.loads((data / "expected_findings.json").read_text())}
    catalog = json.loads((data / "assessment_catalog.json").read_text())
    rows = [{"case_id": c["case_id"], "input": c["input"], "expected": expected[c["case_id"]],
             "source": c["source"], "business_risk": c["business_risk"]} for c in cases]
    client = weave.init(PROJECT)
    dataset = weave.Dataset(name="bank-vendor-scope-five-v1", rows=rows,
                            description="Five synthetic cases and draft expected findings; user review pending. Not measured vendor behavior.")
    ref = weave.publish(dataset)
    client.flush()
    loaded = list(weave.ref(ref.uri()).get().rows)
    if len(loaded) != 5 or {r["case_id"] for r in loaded} != {r["case_id"] for r in rows}:
        raise RuntimeError("Dataset readback failed")
    output_dir = ROOT / "review_output"
    output_dir.mkdir(exist_ok=True)
    receipt = {"dataset_uri": ref.uri(), "rows_verified": len(loaded), "manifest": manifest,
               "git_commit": os.environ.get("GITHUB_SHA"), "sample_status": "not_requested",
               "evaluations_run": False, "judge_implemented": False, "v2_implemented": False}
    dataset_url = f"https://wandb.ai/{PROJECT}/weave/objects/{ref.name}/versions/{ref.digest}"
    receipt["dataset_url"] = dataset_url
    (output_dir / "publication.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(f"Published and read back {len(loaded)} cases: {ref.uri()}")
    summary = ["# Review package", f"Dataset: {ref.uri()}", f"[Open dataset]({dataset_url})",
               "Five synthetic rows read back successfully. Expected findings await human review."]
    try:
        if args.sample:
            reviewer = VendorReviewer(catalog=catalog)
            result, call = reviewer.predict.call(input=cases[0]["input"])
            client.flush()
            recorded = client.get_call(call.id)
            trace_url = f"https://wandb.ai/{PROJECT}/weave/calls/{call.id}"
            receipt["sample_trace_url"] = trace_url
            if call.exception or recorded.exception or not result:
                receipt["sample_status"] = "failed; inspect trace"
                summary += [f"V1 sample failed. [Inspect trace]({trace_url})"]
                raise RuntimeError("V1 inference sample failed; dataset publication succeeded")
            if recorded.output != result:
                raise RuntimeError("Sample trace output readback mismatch")
            scores = {"reference_integrity": score_references(cases[0]["input"], result),
                      "status_and_routing": score_status(cases[0]["input"], result)}
            sample = {"case_id": "C01", "application_version": "v1", "model": reviewer.model,
                      "temperature": 0, "scores": scores, "assessment": result,
                      "trace_url": trace_url, "dataset_uri": ref.uri(),
                      "notice": "One actual model-generated draft on synthetic input; no AI judge or V1/V2 comparison yet."}
            (output_dir / "v1-C01.json").write_text(json.dumps(sample, indent=2), encoding="utf-8")
            receipt["sample_status"] = "generated_and_read_back"
            receipt["sample_scores"] = scores
            summary += [f"[Open V1 C01 trace]({trace_url})", "Exact-rule scores: " + json.dumps(scores),
                        "A passing exact-rule score does not establish semantic correctness. Review the draft and expected findings."]
    finally:
        client.flush()
        (output_dir / "publication.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        (output_dir / "REVIEW.md").write_text("\n\n".join(summary), encoding="utf-8")
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
                handle.write("\n\n".join(summary))
        weave.finish()


if __name__ == "__main__":
    main()
