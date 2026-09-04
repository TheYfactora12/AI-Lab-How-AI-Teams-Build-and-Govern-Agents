# Public-document intake and traceability

This extension tests the intake foundation for the proposed risk-review workflow. Three public publisher-hosted documents were downloaded on September 4, 2026. Original files are in the local public_source_cache/ folder. They are not committed or uploaded to Weave; metadata and hashes are. Public availability is not a transfer of copyright.

## Source collection

| Document | Observed scope | Why included |
| --- | --- | --- |
| [Cloudflare SOC 3](https://www.cloudflare.com/resources/assets/slt3lc6tev37/68oHQbiMBGK65EKiyHgWvh/6685231d288258b0618410632063e1eb/Cloudflare-SOC3-Report.pdf) | 16-page report; May 1–October 31, 2019; Global Cloud Platform for Enterprise Customers | Historical evidence must not be represented as current AI assurance |
| [AWS SOC 3](https://d1.awsstatic.com/whitepapers/compliance/AWS_SOC3.pdf) | 55-page report; April 1, 2024–March 31, 2025; AWS system | Separate vendor identity and service-scope exclusions |
| [Cloudflare Workers AI data-use documentation](https://developers.cloudflare.com/workers-ai/platform/data-usage/) | Vendor-published web documentation, captured as HTML | Vendor statements are a different evidence type from an auditor's report |

Report periods above were checked against the downloaded PDF cover text. Search metadata called the Cloudflare report a draft; do not infer report status from a search title. Neither report automatically establishes suitability for our fictional bank use case. Sources retain their real vendor identities; do not relabel them as CedarBridge evidence.

## Provenance chain

1. data/public_sources.json declares the source ID, publisher/vendor, URL, format and test purpose.
2. data/public_source_manifest.json freezes exact downloaded bytes with SHA-256, retrieval time, resolved URL, content type, byte count and PDF extraction counts.
3. bank_review/intake.py re-downloads sources and compares them with that manifest. A changed URL response fails the fingerprint check; it is not silently substituted into the experiment.
4. GitHub Actions records its source commit and executes local structural tests.
5. The Weave verify_batch call contains the source-code hash, manifest hash, registry hash, workflow run ID and nested verify_document calls.
6. A versioned Weave dataset stores source metadata. The workflow reads back the trace and dataset hashes and saves a receipt with their exact references.

A hash proves byte identity against our captured reference; it does not prove that a vendor's claims are true. Metadata inspection also does not establish accurate semantic extraction from every PDF page. Source downloads and parsing occur before the traced verification batch; network/parser failures currently appear in GitHub logs, not as nested Weave download calls. That is a known observability limit to address before production intake.

## Structural tests and boundaries

Six intake tests cover valid provenance without assessment permission, wrong vendor, changed content at the same URL, duplicate content, no extracted PDF text and missing provenance. Existing assessment calibration is also run. These are implementation tests, not LLM quality scores.

Batch validation blocks duplicate content and rejects missing batches. Real download verification checks the three source records; negative cases use test metadata and do not alter the public reports. A source document's embedded instructions remain untrusted data; this intake code does not execute them.

No model is called by this workflow. No report conclusions, controls, residual risk or automation eligibility have been evaluated on these public sources yet. The frozen original five-case V1/V2 comparison remains unchanged.

Before a model comparison, add page-addressable extraction, a fictional intended-use profile kept separate from source facts, explicit expected findings reviewed by a person, and test cases for scope, dates, missing evidence and routing. Freeze a new evaluation contract. Rate our agent's interpretation, not the real vendor as a whole.

## Run or inspect it

Verified run on September 4, 2026: all three fingerprints passed, the trace and dataset were read back successfully, and 17 existing plus six intake tests passed. No inference calls occurred.

- [Open the actual Weave intake trace](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cee-1c4a-79f9-8b7f-cc01ad29be0a)
- [Open the exact metadata dataset version](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/public-document-intake-v1/versions/4SWk5HsTS0iUjKDIYXzZE6q7kVOGeXZUVYnNgyXFv2I)
- [Successful GitHub execution](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33886786883)
- [Saved receipt with code and source fingerprints](intake_snapshots/first/receipt.json)

Executed code commit: 229c67798afd0af19ce4a6d5e331b9e5db46ea1b. The receipt's source-code hash refers to bank_review/intake.py. Git hashes use the repository's normalized file bytes; locally checked-out line endings may differ.

Open [GitHub Actions](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/workflows/public-document-intake.yml) and select **Verify public document intake**. The workflow uses existing secret W_B and performs no inference calls. The final step prints the Weave trace and dataset references; download public-intake-receipt for the machine-readable record.

Locally, install requirements-intake.txt. Run `python -m unittest discover -s intake_tests -v`. With W&B authentication configured, run `python -m bank_review.intake --publish`. The initial collection command deliberately refuses to overwrite an existing manifest. HTML can change between requests; a fingerprint block requires inspection and explicit versioning, not a bypass.

## Beginner demonstration route

1. Open the intake receipt's trace_url. This opens the recorded Weave call directly.
2. Inspect verify_batch inputs: document IDs, source URLs and byte fingerprints identify exactly what was checked.
3. Expand a verify_document child. Its input is the observed metadata and frozen expectation; its output gives pass/block with reasons.
4. Return to the parent output. Find git_commit and workflow_run in build; use the commit in GitHub to see the implementation that produced this result.
5. Open the dataset reference in the project dataset/object view to inspect the captured metadata. The original PDFs remain local or at their source links.
6. Explain: this proves our intake record is traceable. Then open the separate V1/V2 links in COMPARISON_REPORT.md to show assessment evaluation. Do not describe these as one end-to-end public-vendor assessment yet.

W&B navigation labels can vary; saved direct trace links are the starting point. The dataset reference identifies a version even if the interface changes.
