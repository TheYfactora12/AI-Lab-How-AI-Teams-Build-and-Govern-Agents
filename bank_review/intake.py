"""Public-document provenance and structural checks; not a vendor assessment."""
import argparse
from datetime import datetime, timezone
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

from pypdf import PdfReader
import weave

ROOT = Path(__file__).resolve().parents[1]
PROJECT = "kevinmedeiros-masterclass/ai-lab-agent-governance"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def download(source):
    request = Request(source["url"], headers={"User-Agent": "AI-Lab-Public-Document-Review/1.0"})
    with urlopen(request, timeout=60) as response:
        data = response.read(25_000_001)
        if len(data) > 25_000_000:
            raise ValueError("Source exceeds intake size limit")
        result = {**source, "resolved_url": response.url,
                  "retrieved_at": datetime.now(timezone.utc).isoformat(),
                  "content_type": response.headers.get("Content-Type"),
                  "sha256": digest(data), "byte_count": len(data)}
    if source["format"] == "pdf":
        if not data.startswith(b"%PDF-"):
            raise ValueError("Expected PDF signature")
        reader = PdfReader(BytesIO(data))
        result["page_count"] = len(reader.pages)
        result["text_character_count"] = sum(len(p.extract_text() or "") for p in reader.pages)
        if not result["text_character_count"]:
            raise ValueError("No extractable text; OCR/manual review needed")
    else:
        if "html" not in (result["content_type"] or ""):
            raise ValueError("Expected HTML")
    return data, result


def validate_record(record, expected, target_vendor, seen_hashes=()):
    reasons = []
    if record.get("vendor_id") != target_vendor:
        reasons.append("vendor_mismatch")
    for field in ("document_id", "sha256", "url", "format"):
        if not record.get(field) or record.get(field) != expected.get(field):
            reasons.append(f"{field}_mismatch")
    if not record.get("retrieved_at") or not record.get("byte_count"):
        reasons.append("incomplete_provenance")
    if record.get("sha256") in seen_hashes:
        reasons.append("duplicate_content")
    if record.get("format") == "pdf" and not record.get("text_character_count"):
        reasons.append("text_unavailable")
    return {"status": "block" if reasons else "pass", "reasons": reasons,
            "assessment_permission": False}


@weave.op()
def verify_document(record: dict, expected: dict, target_vendor: str) -> dict:
    return validate_record(record, expected, target_vendor)


@weave.op()
def verify_batch(records: list, manifest: list, build: dict) -> dict:
    if not manifest or len(records) != len(manifest):
        raise ValueError("Missing intake records")
    checks = [verify_document(r, e, e["vendor_id"]) for r, e in zip(records, manifest, strict=True)]
    hashes = [r["sha256"] for r in records]
    if len(hashes) != len(set(hashes)):
        checks.append({"status": "block", "reasons": ["duplicate_content"]})
    return {"checks": checks, "all_passed": all(x["status"] == "pass" for x in checks),
            "build": build, "meaning": "Provenance checks only; no risk rating or model evaluation"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true", help="Create a new source manifest locally")
    parser.add_argument("--publish", action="store_true", help="Verify downloads against frozen manifest and log to Weave")
    args = parser.parse_args()
    if args.collect == args.publish:
        parser.error("Choose exactly one of --collect or --publish")
    sources = json.loads((ROOT / "data/public_sources.json").read_text(encoding="utf-8"))
    cache = ROOT / "public_source_cache"
    cache.mkdir(exist_ok=True)
    records = []
    for source in sources:
        data, record = download(source)
        (cache / f"{source['document_id']}.{source['format']}").write_bytes(data)
        records.append(record)
    manifest_path = ROOT / "data/public_source_manifest.json"
    if args.collect:
        if manifest_path.exists():
            raise FileExistsError("Version the existing manifest before collecting again")
        manifest_path.write_text(json.dumps(records, indent=2), encoding="utf-8")
        print("Downloaded three public sources and froze their fingerprints.")
        return
    expected = json.loads(manifest_path.read_text(encoding="utf-8"))
    build = {"git_commit": os.environ.get("GITHUB_SHA"), "workflow_run": os.environ.get("GITHUB_RUN_ID"),
             "intake_sha256": digest(Path(__file__).read_bytes()),
             "manifest_sha256": digest(manifest_path.read_bytes()),
             "source_registry_sha256": digest((ROOT / "data/public_sources.json").read_bytes())}
    client = weave.init(PROJECT)
    try:
        result, call = verify_batch.call(records, expected, build)
        dataset_ref = weave.publish(weave.Dataset(name="public-document-intake-v1", rows=records))
        client.flush()
        saved = client.get_call(call.id)
        loaded = list(weave.ref(dataset_ref.uri()).get().rows)
        if saved.exception or saved.output != result or len(loaded) != len(records):
            raise RuntimeError("Weave readback mismatch")
        if [r["sha256"] for r in loaded] != [r["sha256"] for r in records]:
            raise RuntimeError("Published document identity mismatch")
        receipt = {"trace_url": f"https://wandb.ai/{PROJECT}/weave/calls/{call.id}",
                   "dataset_uri": dataset_ref.uri(), "result": result,
                   "original_files_uploaded": False, "model_calls": 0}
        output = ROOT / "intake_output"
        output.mkdir(exist_ok=True)
        (output / "receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        print(json.dumps(receipt, indent=2))
        if not result["all_passed"]:
            raise RuntimeError("Source changed or failed provenance checks; inspect trace")
    finally:
        weave.finish()


if __name__ == "__main__":
    main()
