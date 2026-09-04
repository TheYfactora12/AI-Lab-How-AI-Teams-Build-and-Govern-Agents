# V2: Evidence-validation gate

Status: Planned, not an observed improvement.

The certificate calls for one targeted application change under fixed evaluation conditions. Our deeper fix is one coherent post-generation validation mechanism.

Source: https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/TECHNICAL_TRACK.md

## V1 baseline

A live model drafts the structured assessment from the use-case profile, catalog and evidence. The shared prompt requests grounded answers. V1 has no post-generation evidence gate. Do not deliberately instruct it to fabricate facts or hard-code failure.

Hypothesis: It may mistake a vendor assertion or architecture description for tested behavior. Actual evaluations must determine whether this happens. If V1 passes, report that rather than claiming a gain that was not measured.

## One targeted V2 change

Add a deterministic gate for claims marked `tested_in_scope`. Resolve cited records from the actual supplied packet and check:

1. Retrieval succeeded and the cited passage exists.
2. Evidence type is `observed_test_result`.
3. Vendor, use case, requirement and system version match.
4. Evidence is current under the fixture's explicit date rules.
5. A test method, passing result and limitations are present.

Missing evidence cannot be invented. If a check fails, retain the original draft in the trace, withhold its unsupported conclusion from the final packet, and return a structured evidence request requiring human review. Changing a label while leaving the unsupported favorable narrative in the final report is insufficient.

This is structural validation. It does not establish record authenticity or prove that every sentence follows from a test. The independent judge still assesses semantic support. It does not automatically fix the scope ambiguity in C03 or the training contradiction in C05.

## Shared output contract to implement

- `scope`: requirement ID, applicability and rationale.
- `findings`: requirement ID, claim, evidence status and citations.
- `questions`: evidence requests and accountable owners.
- `packet_status`: ready_for_human_review, needs_evidence or withheld.
- `human_review_required`: true for this prototype.
- `pilot_approved`: false for this prototype.
- `gate_record`: applied/not_applied plus checks, reasons and affected requirements.

Applicability values: applicable, not_applicable, needs_clarification. Evidence statuses: asserted, documented, tested_in_scope, missing, retrieval_error, conflicting. Orchestration attaches the case ID. V1 and V2 share the schema; V1 records that the gate was not applied. Record both the original model draft and final output in the trace.

## Independent scoring design

**Evidence reference integrity:** Valid citation and passage IDs with correct vendor/use-case binding pass. Known invalid references fail. Missing trace/input evidence necessary to decide produces unknown. A finding explicitly acknowledging absent evidence does not require an invented citation. Citation meaning is assessed by the judge.

**Evidence status and routing consistency:** Test claims must satisfy the metadata checks above, and missing/failed evidence must not be cleared as verified. Contradictory evidence status or routing fails. Missing fields needed to decide produce unknown. Correctly reporting a failed retrieval can pass.

A known failure takes precedence over unrelated missing fields. Implement pass/fail/unknown fixtures for each scorer. Keep scorer code independent of the application gate to reduce correlated mistakes.

The live judge will have exactly three criteria:

| Criterion | Blocking? | What it examines |
| --- | --- | --- |
| Evidence support | Yes | Conclusions and assurance level follow from cited evidence |
| Scope and material-risk coverage | Yes | Applicability fits intended use; important gaps and contradictions are surfaced |
| Follow-up quality | No | Questions are specific, actionable and proportionate |

Per-criterion pass means satisfied, fail means demonstrated violation, unknown means insufficient evidence to judge. Blocking failure yields block; otherwise unknown or nonblocking failure yields review; all pass yields pass. Deterministic failures cannot be overridden by the judge. Expand these into detailed rubric rules before implementation.

## Controlled comparison

Keep application model, parameters, base prompt, scope logic, retrieval, schemas, dataset, scorer set, rubric, judge model and release policy fixed. Only the evidence gate changes. Pin all versions before live comparison; model access and exact model selection are still pending.

C02 is the primary target; C04 checks the related unavailable-evidence path. C01, C03 and C05 are regression checks. Report each case, not just an average. Improvement requires an actual targeted V1 failure corrected by V2 without losing normal-case quality. No observed failure means no demonstrated gain on this dataset.

Further prompt changes, model swaps and broader fixes belong in a separate experiment. Five cases do not establish a production failure rate or broad market advantage.
