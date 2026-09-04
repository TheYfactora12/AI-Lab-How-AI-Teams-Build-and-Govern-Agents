# Stress review: passing calibration does not establish robustness

The original 17 assessment tests and six intake tests passed again. An additional 23 offline probes produced 14 expected outcomes and nine gaps. These counts are probe outcomes, not nine independent defects or a production failure rate.

This run made no model calls and created no new Weave evaluation. It stress-tested component behavior and replayed saved judgments. [Raw probe results](stress_snapshots/offline-review.json) record each input mutation, expected status, observed result, source revision and script fingerprint. [Reproducible runner](scripts/stress_review.py) executes with `python scripts/stress_review.py` after dependencies are installed.

## Findings that matter

| Finding | Observed evidence | Interpretation |
| --- | --- | --- |
| Null document entries | Status scorer raised AttributeError; gate raised TypeError | Nested input validation is incomplete at these component boundaries |
| Null passage collection | Status scorer passed; gate raised TypeError | Status metadata checks alone do not establish usable passage evidence; gate is not robust to this malformed source |
| Conflicting duplicate source IDs | Status scorer passed and gate kept ready_for_human_review | Dictionary indexing silently selects the later record; ambiguous source identity should be rejected |
| Null finding | Status scorer raised AttributeError | Direct component invocation is not resilient to malformed findings; the normal model schema may reject this earlier |
| Known C03 scope error | Both saved combined judgments still returned pass | Confirms the previously documented coverage gap; no fresh model response was generated |

The two saved C03 judgments account for two of the nine gaps. Multiple probes exercise the same defect. A status-scorer pass on null passages is not proof that the complete workflow passes: another scorer or an exception can prevent completion. These probes invoke components directly; they do not establish reachability through every normal application path or demonstrate real cross-vendor disclosure.

## What continued to work

Wrong vendor identity, mismatched test requirements, unavailable test evidence, missing test method and malformed dates were rejected or marked unknown by the status scorer and withheld by the gate. Empty findings produced unknown; unauthorized pilot approval failed. Missing judge results routed to review, and an exact failure overrode a favorable judge.

The six existing intake tests still passed. This run did not re-download the public documents, stress network concurrency, or test new intake scenarios. It is not a load/performance test or a fresh V1/V2 hosted comparison.

## Decision and next fix

Continue draft-only use with human review. Before accepting less controlled document packets, prioritize validation of nested record shapes and unique source identifiers, then add explicit unknown-scope checks. Verify the complete error path so component failures produce an inspectable unresolved result rather than losing scoring evidence.

Application code, original scorers, dataset and frozen contract were not changed in this stress review. Fixes to shared code/scorers require a new contract and a rerun of both application versions. Preserve this result and the original comparison as the before evidence. Do not change expectations to label these probes successful.

The simplified comparison's per-case verdicts were checked against the original snapshots, and the experiment file fingerprints remain unchanged. This report supplements [the comparison](COMPARISON_REPORT.md); it does not replace the stored model evaluation results.
