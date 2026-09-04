# Saved review package

The dataset is published, V1 has generated one actual assessment, and the original output is saved for review. No live judge or full V1/V2 evaluation has run.

For the full context, see [the project record and references](docs/PROJECT_RECORD.md) and [class notes](docs/CLASS_NOTES.md).

## Open the work

- [Five-case dataset in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs)
- [Actual V1 C01 trace](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06a6e-a2aa-7fcf-aaa4-51c2c8cfc45f)
- [Successful GitHub workflow](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33832814085)
- [Saved original V1 output and exact-rule scores](review_snapshots/v1-C01.json)
- [Publication receipt and fingerprints](review_snapshots/publication.json)
- [Expected findings for all five cases](data/expected_findings.json)

Use the dataset/object and Calls/Traces views in Weave. The Agents sessions page may remain empty because this application uses function tracing.

## Confirmed results

The workflow ran ten local scorer-calibration tests successfully, published and read back five dataset rows, and generated a V1 assessment using `OpenPipe/Qwen3-14B-Instruct` through W&B Serverless Inference. The root trace output was read back and matched the generated result. Both deterministic scorers returned pass on C01.

The actual sample used code commit `688f7cd`. Its full commit SHA and dataset file hashes are in the publication receipt. Later documentation commits do not change that recorded sample.

## Findings for our human review

These observations are from inspecting the saved output, not a live AI-judge evaluation.

1. **Applicability selection:** V1 listed nine applicable requirements and excluded credit-decision testing, consistent with the C01 expected scope. Some rationales rely on the presence of evidence rather than the underlying use-case risk; that reasoning should be discussed before the full comparison.
2. **Overbroad assurance language:** The SEC-01, SEC-02, SEC-03 and QUAL-01 claims use wording such as “ensures.” Their evidence covers a configuration snapshot or limited synthetic tests. Exact source validity checks passed, but those checks do not establish that this broad wording is justified. The evidence-support judge must assess this distinction.
3. **Packet-state mismatch:** V1 returned `needs_evidence`; the C01 answer key expects `ready_for_human_review`. The output asks for broader testing and accessibility results. Decide whether this is appropriate caution or unnecessary escalation against our stated draft-review boundary. Do not silently change the expected answer to match the model.
4. **Question quality:** Accessibility questions are duplicated and one is assigned to QUAL-01 rather than FAIR-01. Some questions ask for information already partly supplied. The judge should examine specificity and proportionality.
5. **Human authority preserved:** V1 required human review and did not approve the pilot.

Passing these two scorers is not a claim that the assessment is correct or the vendor is safe. A good reference can still be used to support an overstatement.

## Preserve the baseline

The saved sample is unedited. V2 remains the planned evidence-validation gate; the broader wording issue may exceed that gate's structural checks. Discuss the intervention before freezing the comparison. Any revision to catalog, input cases, expected findings, rubric or policy requires consistent reevaluation of both versions.

## Next review session

Review the normal-case packet and its expected findings first. Then review the missing-test, ambiguous-scope, timeout and contradiction cases. Finalize the output semantics and detailed three-criterion judge rubric, freeze the contract, implement V2, and run both versions on the exact same published dataset.

The original JSON is committed to GitHub for durable review. The Actions artifact is also downloadable for 90 days; W&B retention follows account settings.
