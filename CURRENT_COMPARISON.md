# Current V1/V2 comparison: documentary boundaries and fail-closed behavior

**Presentation decision: draft-only use with human review.** Contract 1.4 shows that V2 contains the tested unknown-scope and citation-boundary problems. It also shows that model generation can still fail. The workflow routes invalid output to review instead of releasing it.

This is contract **bank-vendor-eval-v1.4**. V1 and V2 used the same five synthetic cases, prompt, model, exact scorers and judge. V2 alone adds the post-generation validation gate. Earlier contracts remain historical evidence and are not pooled into these counts.

## Open the current evidence

- [Current V1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fc-9244-721f-894e-d4bb3ecf9ec1)
- [Current V2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fd-071e-7eeb-8a8f-fe0cf744302a)
- [Successful GitHub Actions execution](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33972108376)
- [Receipt and source fingerprints](evaluation_snapshots/contract-1.4/receipt.json)
- [V1 outputs and scores](evaluation_snapshots/contract-1.4/v1-rows.json), [V2 outputs and scores](evaluation_snapshots/contract-1.4/v2-rows.json)
- [31-probe offline stress result](stress_snapshots/corrected-review.json)

## What happened

| Case | V1 verdict | V2 verdict | Inspection and meaning |
| --- | --- | --- | --- |
| C01: normal packet | Pass | Pass | Both return `needs_evidence` although the answer key expects a review-ready draft. This is safe over-escalation. |
| C02: missing role test | Pass | Pass | Both return `ready_for_human_review` although the answer key expects `needs_evidence`. The graders still miss this readiness error. |
| C03: unknown scope | Block | Block | V1 makes unsupported scope decisions. V2 withholds the draft and records three rejections: two unknown-scope decisions and one requirement-mismatched citation. |
| C04: retrieval timeout | Pass | Pass | Both disclose the unavailable evidence and request follow-up. |
| C05: contradictory evidence | Block | Review | V1 produces a valid unresolved assessment, but the judge blocks it with unreliable reasoning that calls the disclosed conflict invented and incorrectly says V1 withheld the draft. V2's separate generation is schema-invalid; the error envelope withholds it and the judge is not invoked. |

V1 has **3 passes and 2 blocks with zero application errors**. V2 has **3 passes, 1 block and 1 review with one application error**. These are assessment-quality routing results, not vendor approvals or production error rates.

## What the stress test found and fixed

The first 23-probe suite passed, but an independent test changed a cited record from `tested_in_scope` to `documented`. Before this correction, eight bad documentary-evidence variants could reach `ready_for_human_review`: wrong vendor, wrong use case, missing source, invented quote, unavailable source, wrong requirement binding, stale evidence and wrong system version.

V2 now applies source identity, use-case, version, availability, requirement, date-window and exact-quote checks to every cited finding. The permanent offline suite contains **31 probes with zero observed gaps**. The checks made no model calls and are not 31 additional evaluation cases.

This verifies the tested rules. It does not prove source authenticity, semantic truth, resistance to every malformed input or production reliability.

## The C03 demonstration

1. Open V1 C03 and show `restricted_documents=null` and `credit_decisions=null`.
2. Show V1 treating those unknown fields as definite scope decisions. The exact status scorer blocks them.
3. Open V2 C03 and expand `gate_record`.
4. Show the three rejected findings, `packet_status: withheld`, clarification questions and mandatory human review.
5. Explain that the original model draft stays visible in the trace for audit, while the released packet is withheld.

The third rejection is a USE-01 finding citing evidence bound to a different requirement. This is direct hosted evidence that the expanded citation gate operated in a real run.

## Limits that must be stated

- There is one hosted trial per case. Temperature zero does not guarantee identical hosted outputs.
- V2 C05 failed schema validation while V1 C05 succeeded. The fail-closed path worked, but generation reliability remains unresolved.
- C02's readiness error still passes both exact checks and the AI judge.
- V1 C05 shows that the judge can misread a correctly disclosed contradiction; its model verdict and mechanically enforced verdict also disagree.
- The rule set covers this fictional internal-policy-assistant use case; it is not a complete banking GRC framework.
- The answer key is AI-assisted and has not received independent expert validation.
- All outputs remain drafts for human review. No automatic vendor approval or risk acceptance is authorized.

## Verification status

- 23 assessment regression tests passed.
- Six intake tests passed.
- 31 offline adversarial probes met their stated expectations.
- The hosted workflow completed and read both Weave evaluation summaries back successfully.
- Contract 1.3 is preserved as an intermediate run that exposed generation variability; contract 1.4 is the current presentation evidence.

Use this page for current counts and links. Use [the correction record](V2_CORRECTION_RECORD.md) for the change history and [the recording cheat sheet](RECORDING_CHEAT_SHEET.md) for the four-minute explanation.
