# V2 correction record: contract 1.2

The offline stress review found malformed-input exceptions and conflicting duplicate source IDs. The earlier live comparison also exposed incorrect scope decisions and judge reasoning about an unavailable output. This revision addresses those specific paths without deleting the earlier evidence.

## Changes and attribution

| Change | Applies to | Why |
| --- | --- | --- |
| Validate nested source records, passages and citations | Both versions and exact scorers | Reject malformed inputs and ambiguous source identity instead of crashing or silently selecting a duplicate |
| Explicit finding-status instruction | Both versions' shared prompt | Clarify that not_applicable belongs in scope, never the finding evidence-status enum; invalid outputs are still withheld, not silently repaired |
| Exact conditional scope checks | Same scorer for both versions | Detect contradictions between SEC-01/FAIR-02 scope and supplied intended-use fields |
| Error-envelope judge precondition | Same judge for both versions | Return unknown/review without a model call when no valid assessment exists |
| Evidence and scope validation gate v2.0 | V2 only | Withhold unsupported generated content and preserve unresolved conditional scope |

The difference within the new comparison is the post-generation validation gate. Shared prompt/scorer/judge corrections mean this experiment is not interchangeable with contract 1.1. Compare the new V1 against the new V2. Do not attribute shared improvements to the V2 gate.

The original five inputs and expected findings are unchanged. Models and inference parameters are unchanged. The [new contract](evaluation_contract.json) records exact source fingerprints. The original contract remains embedded in the [old receipt](evaluation_snapshots/final/receipt.json), and the old code remains available through its recorded commit.

## Regression evidence

The corrected run passes 22 assessment regression tests plus six intake tests. All 23 offline stress probes now meet their expectations; the two C03 replay probes apply current exact rules to old outputs while retaining the old judge scores. [Corrected raw stress results](stress_snapshots/corrected-review.json) are separate from the [original failures](stress_snapshots/offline-review.json). These are not 23 additional live model cases.

[Hardening tests](tests/test_v2_hardening.py) cover malformed document/passage/finding shapes, duplicate source records in both orders, rejection before model invocation, the no-model error judge, and replay of the actual C03 outputs. The scope replay proves that corrected rules detect the old failure and that V2 withholds it; it is not a new model assessment.

Structural validation is shared plumbing. Evidence eligibility and scope enforcement are separate code in the scorer and gate, so their substantive checks do not simply call one another. This design still cannot prove a source's authenticity or all semantic support.

## Limits retained

- Two conditional requirements are checked against explicit profile fields; this is not a general risk-classification engine.
- Whole-packet withholding can reduce useful coverage.
- The judge may still misgrade valid outputs; the error precondition fixes only unavailable-output handling.
- A prompt clarification does not guarantee valid JSON in future trials.
- No automatic vendor approval, risk acceptance or client-facing release is authorized.
- Public-document assessment and calibrated numerical risk ratings remain outside this completed five-case comparison.

Live rerun results and presentation links will be recorded in the current comparison report. The historical experiment remains available for the before/after story.
