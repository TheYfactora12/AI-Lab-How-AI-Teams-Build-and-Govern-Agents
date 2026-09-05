"""Verify local presentation links and bind current external evidence URLs to receipts."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "README.md", "GITHUB_RECORDING_GUIDE.md", "START_DEMO_HERE.md",
    "CURRENT_COMPARISON.md", "VIDEO_WALKTHROUGH.md", "SUBMISSION_CHECKLIST.md",
    "RECORDING_CHEAT_SHEET.md",
]
REPO = "TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents"
CURRENT_RECEIPT = ROOT / "evaluation_snapshots/contract-1.4/receipt.json"


def links(path):
    return re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8"))


def main():
    checks, failures = [], []
    for name in FILES:
        path = ROOT / name
        for target in links(path):
            check = {"source": name, "target": target}
            if target.startswith("#"):
                heading = unquote(target[1:]).replace("-", " ").lower()
                content = path.read_text(encoding="utf-8").lower()
                ok = any(line.lstrip("# ").strip() == heading for line in content.splitlines() if line.startswith("#"))
                method = "local_heading"
            elif "://" not in target:
                ok = (path.parent / target.split("#")[0]).exists()
                method = "local_file"
            else:
                parsed = urlparse(target)
                marker = f"github.com/{REPO}/blob/main/"
                if marker in target:
                    repo_path = unquote(target.split(marker, 1)[1].split("#", 1)[0])
                    ok = (ROOT / repo_path).exists()
                    method = "github_blob_matches_repository"
                elif parsed.netloc == "github.com" and f"/{REPO}/actions/runs/" in parsed.path:
                    receipt = json.loads(CURRENT_RECEIPT.read_text())
                    ok = parsed.path.rstrip("/").endswith(f"/actions/runs/{receipt['workflow_run']}") and receipt["complete"]
                    method = "github_run_matches_completed_receipt"
                elif parsed.netloc == "github.com" and parsed.path.rstrip("/") == f"/{REPO}":
                    ok, method = True, "repository_identity"
                elif parsed.netloc == "wandb.ai" and "/weave/calls/" in parsed.path:
                    receipt = json.loads(CURRENT_RECEIPT.read_text())
                    ok = target in {receipt["runs"][v]["trace_url"] for v in ("v1", "v2")}
                    method = "private_weave_url_matches_readback_receipt"
                else:
                    ok, method = True, "external_reference_not_network_tested"
            check.update(ok=ok, method=method)
            checks.append(check)
            if not ok:
                failures.append(check)
    result = {"scope": FILES, "check_count": len(checks), "failure_count": len(failures),
              "network_note": "Private W&B accessibility depends on signed-in project access. URLs are matched to the successful readback receipt; no public-access claim is made.",
              "checks": checks}
    output = ROOT / "presentation_snapshots"
    output.mkdir(exist_ok=True)
    (output / "link-check.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Checked {len(checks)} presentation links; failures: {len(failures)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
