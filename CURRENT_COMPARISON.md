# Current V1/V2 comparison: corrected validation, remaining judgment limits

**Presentation decision: draft-only use with human review.** The corrected V2 catches the observed unknown-scope error and withholds the assessment. It handles the tested malformed-input and duplicate-source cases safely. It is not a fully reliable autonomous reviewer.

This is contract **bank-vendor-eval-v1.2**, separate from the original contract 1.1. Both versions were rerun on the same five original synthetic cases, using the same updated shared prompt, scorers and judge. The only difference within this pair is V2's post-generation validation gate. Read the [change record](V2_CORRECTION_RECORD.md) for attribution.

## Open the current evidence

- [Current V1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06d7e-b22d-7497-a050-15150061f01b)
- [Current V2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06d7f-274c-7f26-8385-6c4dabf64fbd)
- [Successful execution](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33901467965)
- [Receipt and source fingerprints](evaluation_snapshots/contract-1.2/receipt.json)
- [Original V1 outputs and scores](evaluation_snapshots/contract-1.2/v1-rows.json), [V2 outputs and scores](evaluation_snapshots/contract-1.2/v2-rows.json)

## What matters

| Case | V1 automated verdict | V2 automated verdict | Inspection and next action |
| --- | --- | --- | --- |
| C01: normal packet | Pass | Pass | Both still return needs_evidence instead of the expected draft-review state. Review unnecessary escalation. |
| C02: missing role test | Pass | Pass | Both now use documentary evidence instead of substituting the wrong test. However, ready_for_human_review conflicts with the expected needs_evidence state. The graders miss this readiness issue. |
| C03: unknown scope | Block | Block | V1's scope error is now caught by the exact scorer. V2 corrects the two affected scope fields to needs_clarification and withholds the draft. Its exact status check passes, but the judge blocks. |
| C04: retrieval timeout | Pass | Pass | Both disclose the unavailable evidence and request follow-up. |
| C05: contradictory evidence | Block | Block | Both now produce valid assessments and show the contradiction. The judge still misreads what the evidence establishes. Human adjudication is required. |

Both versions have **3 automated passes and 2 blocks**, but these are different blocked cases from the old comparison. Both have **zero application errors** in this run. V2's gate rejects two scope decisions within **one case**, C03; this is not two failed cases. These counts do not establish production error rates.

## The improvement to demonstrate: C03

1. Open current V1 and locate C03. Inspect restricted_documents=null and credit_decisions=null in the input profile.
2. Show V1's scope: it treats SEC-01 as applicable and FAIR-02 as not_applicable. The corrected exact scorer reports that these decisions contradict the intended-use fields.
3. Open current V2 C03. Its gate_record contains both rejected scope decisions.
4. Show needs_clarification on those scope entries, the withheld packet, and the questions requesting the bank's intended use.
5. Explain that the original generated narrative remains in the generation trace. Withholding prevents those unsupported conclusions from being used, but also removes useful coverage.

This supports a targeted containment claim. It does not prove that all scope judgments or narrative claims are correct. The gate currently maps two conditional requirements; it is not a full general-purpose risk framework.

## Judge results require interpretation

V2 C03's judge says requirements were excluded even though the final scope marks them needs_clarification. It also calls a missing-evidence finding invented evidence. Those criticisms are unreliable. Reduced coverage from whole-packet withholding is still a real limitation.

C05 contains both a contractual no-training statement and a conflicting vendor assertion. The judge treats the contradiction as if it makes the statement about the contract unsupported. A contradictory assertion does not erase what the supplied contract says. Both sources need reconciliation; the agent should not decide actual vendor behavior from this packet alone. Preserve the raw block and have a reviewer adjudicate it.

The new error-envelope precondition returns unknown/review without a model invocation when an assessment is unavailable. Regression tests verify that path. All five live assessments were valid this time, so that fallback was not exercised in this hosted run.

## Verification and fairness

- 22 assessment regression tests passed in the hosted workflow; six intake tests passed locally.
- 23 offline adversarial probes met their expectations; [raw results](stress_snapshots/corrected-review.json) preserve the distinction between component probes and saved-output replay.
- Inputs and answer key stayed identical to the original dataset.
- Shared changes included structural validation, scope scoring, an enum clarification and the judge error precondition. Improvements across contracts cannot be attributed solely to V2.
- The C02 wrong-test behavior from the first comparison did not recur in either version. Do not present that old event as the current V2 intervention result.
- This is one live trial per case. No independent expert validation, automatic vendor approval or numerical risk calibration is claimed.

## Presentation use

Use this report for current counts and links. Use [the earlier comparison](COMPARISON_REPORT.md) and [original stress report](STRESS_TEST_REPORT.md) only as historical evidence explaining why changes were needed. The [current demonstration handoff](START_DEMO_HERE.md) and [recording outline](VIDEO_WALKTHROUGH.md) follow this revision.

The operating rule remains human-reviewed drafts only. Next work should close the readiness-state checks and calibrate qualitative judging, then freeze another contract and rerun both versions. Do not label these residual issues fixed.
