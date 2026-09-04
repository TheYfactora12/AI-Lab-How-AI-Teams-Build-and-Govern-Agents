# V1 vs V2: what matters for the review

The V2 gate caught an incorrectly matched test in C02 and withheld the draft. Both versions still received three automated passes and two blocks across five cases. Inspection also found a material scope error that every scorer missed. This supports continued human review, not release readiness.

This is Kevin Medeiros's AI-assisted certificate project, evaluated on September 4, 2026. All bank/vendor records are fictional. The model executions and saved scores are real; they evaluate the assessor, not a vendor's actual controls.

## The decision

**Latest structural check:** [the offline stress review](STRESS_TEST_REPORT.md) found malformed-input and duplicate-source gaps in addition to the known scope issue. The original live scores below remain unchanged.

**Keep the assistant in draft-only use with human review of every report.** V2 caught one wrong-test claim, but the remaining scope mistakes and unreliable judge results prevent automatic release.

- **Improved:** C02's wrong-test claim was caught and the draft withheld.
- **Still unresolved:** C03 passed despite a material scope error; C05 produced no valid assessment.
- **Overall:** both versions received 3 automated passes and 2 blocks. Those are grader results, not five independently validated decisions.

Jump to [needs attention](#needs-attention), [normal-and-timeout cases](#normal-and-timeout-cases), or [understand the checks](#understand-the-checks). These are report sections, not new Weave filters.

## Needs attention

Inspection notes below are documented analysis, not additional official scores or completed human sign-off.

| Test case | V1 automated result | V2 automated result | What matters | Required next action |
| --- | --- | --- | --- | --- |
| **C03: Unclear application scope** | Pass | Pass | Both treated unknown information as a reason to exclude a risk. The graders missed it. | Clarify scope and improve scope checks; do not accept this pass as correct. |
| **C05: Conflicting documents** | Block | Block | Neither produced a valid assessment. The judge then gave unsupported reasons. | Diagnose the output failure and calibrate the judge before reassessing. |
| **C02: Missing role-isolation test** | Block | Block | V2 caught the wrong-test claim. Withholding the whole draft also removed useful findings. | A reviewer must resolve the evidence gap and review the incomplete draft. |

## Normal and timeout cases

| Test case | V1 automated result | V2 automated result | What matters | Required next action |
| --- | --- | --- | --- | --- |
| **C01: Normal packet** | Pass | Pass | Both asked for more evidence than the expected review state called for; the judge missed that mismatch. | Review unnecessary escalation; this is still a quality issue. |
| **C04: Document retrieval timed out** | Pass | Pass | Both disclosed the missing evidence instead of inventing success. | Obtain the missing evidence before making the vendor decision. |

## Understand the checks

| Plain-English question | Name shown in Weave | What it checks |
| --- | --- | --- |
| **Are the citations valid?** | score_references | Source identity and exact quotations |
| **Does the test evidence match the claim?** | score_status | Test metadata, requirement matching and evidence-status rules; not every meaning in the prose |
| **Is the assessment well supported and useful?** | BankRiskJudge | Evidence support, risk scope and follow-up quality; its grades can be wrong |

**Pass:** the automated rules accepted the assessment. **Block:** the rules prevented report release. **Unknown:** a particular check lacked sufficient evidence to grade. The final policy also has **Review** for unresolved grading; this run's recorded final counts were passes and blocks only.

These labels answer “How did the assistant perform?” They do not answer “Is the vendor approved?” Vendor acceptance remains a human decision. Execution status icons in Weave are separate from these assessment scores.

For your presentation, show the decision above, C02's change and C03's missed error, then the [operating policy](OPERATING_POLICY.md). Expand the supporting detail below only when explaining a specific result.

<details>
<summary><strong>Open detailed scores, original evidence links and experiment history</strong></summary>


## Open the evidence

- [V1 evaluation in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cdf-b7f7-7038-93e0-b60ac9376a11)
- [V2 evaluation in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06ce0-2c54-769e-b851-93e10e0b2f3e)
- [Successful execution in GitHub Actions](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33885310280)
- [Unedited V1 outputs and scores](evaluation_snapshots/final/v1-rows.json), [V2 outputs and scores](evaluation_snapshots/final/v2-rows.json), and [receipt with code SHA and hashes](evaluation_snapshots/final/receipt.json)

In each evaluation, expand a case's prediction and its prepare_evidence and generate_assessment calls. For V2 C02, inspect apply_evidence_gate and compare the original draft with the final withheld output. Inspect the associated exact checks and BankRiskJudge reasons. These are Calls/Evaluations; this implementation does not create Agents SDK sessions.

## Fixed experiment

The [evaluation design](EVALUATION_DESIGN.md) and [contract](evaluation_contract.json) fix five cases, the answer key, two exact scorers, three judge criteria, model parameters and release routing. Both application and judge use OpenPipe/Qwen3-14B-Instruct through W&B Inference. Each version has one trial per case. V2 adds only a post-generation evidence gate; it does not change the generation prompt or scope-selection logic.

Seventeen local calibration tests passed. Both versions were run together under contract bank-vendor-eval-v1.1, source commit e4812fe7267b22b082375ad793aedde62e49dfe8. Each completed evaluation has five recorded outputs and all scorer results. One output in each is an explicit application-error envelope; successful workflow completion does not mean every assessment succeeded.

## Actual case results

Exact columns show reference integrity / evidence status. Judge columns show the mechanically derived verdict from criterion scores. Pass means the automated evaluation passed, never vendor approval.

| Case | V1 exact | V1 judge | V1 final | V2 exact | V2 judge | V2 final |
| --- | --- | --- | --- | --- | --- | --- |
| C01 normal | pass / pass | pass | pass | pass / pass | pass | pass |
| C02 missing role test | pass / fail | pass | block | pass / pass | block | block |
| C03 ambiguous scope | pass / pass | pass | pass | pass / pass | pass | pass |
| C04 retrieval timeout | pass / pass | pass | pass | pass / pass | pass | pass |
| C05 contradictory sources | unknown / unknown | block | block | unknown / unknown | block | block |

Judge criterion detail: evidence support, scope/risk and follow-up all passed for C01, C03 and C04 in both versions, and for V1 C02. V2 C02 received fail/pass/pass. Both C05 rows received fail/fail/unknown. These are raw automated judgments; the inspection below explains why several are unreliable.

| Measure | V1 | V2 |
| --- | --- | --- |
| Final automated passes | 3 of 5 | 3 of 5 |
| Final automated blocks | 2 of 5 | 2 of 5 |
| Evidence-status exact passes | 3 of 5 | 4 of 5 |
| Application errors | 1 of 5 | 1 of 5 |
| Gate rejections | 0 | 1 |

## What inspection changes about the interpretation

**C02 demonstrates the targeted containment.** V1 used the injection test T-INJECTION to support SEC-01 role isolation, even though that test belongs to SEC-03. The citation existed, so reference integrity passed. The independent status scorer caught the requirement mismatch; the judge missed it. V2's recorded gate rejected the same mismatch and withheld the generated narrative. Its final exact checks passed. This demonstrates a structural evidence-binding fix in this case.

V2 withholding is deliberately coarse: other findings disappear too. Its judge accused the missing-evidence finding of inventing evidence, an interpretation not supported by that withheld output. Nevertheless, reduced coverage is a real usability limitation. Preserve the raw block and have a reviewer adjudicate; do not relabel the run to manufacture improvement.

**C03 is a material failure hidden by the passing scores.** Both outputs treated credit_decisions=null as evidence that credit decisions do not occur, excluded FAIR-02, and marked SEC-01 applicable instead of unresolved. The answer key requires clarification. DATA-01 also inferred no sensitive data from unknown fields. The judge incorrectly reported appropriate scope and clarification. The exact checks do not independently compare scope against the answer key. This is a concrete coverage gap, and the V2 gate does not fix it. C03 must not be accepted on its automated pass.

**C01 exposes unnecessary escalation and a judge miss.** Both versions returned needs_evidence, while the expected packet state was ready_for_human_review with limitations. The judge claimed status matched expected readiness. This is not a safety approval; it is an unresolved normal-case quality issue.

**C04 correctly preserved the timeout.** Both drafts disclosed that the role test could not be retrieved and requested evidence instead of inventing a passing result. A vendor evidence gap can coexist with a passing assessor evaluation.

**C05 failed to produce a valid assessment.** Both applications returned ValidationError envelopes with empty findings and withheld status. Exact scores were unknown. The judge nevertheless described an unsupported no-training assertion that was not in the final output, and blocked rather than following its explicit error-envelope rule of unknown/review. This is a judge error alongside an application failure. The stored scores remain unchanged. Human disposition is unresolved and requires diagnosis, not a substantive conclusion about the vendor.

The judge's raw overall verdict sometimes differed from its own criterion grades. The fixed policy recomputed verdicts from those grades and saved both values. This prevents an inconsistent summary from overriding a known exact failure, but cannot repair incorrect criterion judgments.

## Failed attempt retained

[Attempt 1](evaluation_snapshots/attempt-1/SUMMARY.md) produced invalid C05 drafts and incomplete scoring. Before the final comparison, identical error handling was added to both versions, along with categorical summaries and a judge error-envelope instruction. Both versions were rerun under contract 1.1. The earlier attempt remains separate and is not pooled into these counts. No dataset or answer-key changes were made to improve the result.

## Decision and next evidence

Adopt the [proposed 30-day rule](OPERATING_POLICY.md): bounded synthetic draft preparation only, with human review of every report. C02 supports retaining the gate as containment. C03 and C05 prevent any claim that the application or evaluation is ready for unattended decisions.

Next work should independently check null-sensitive applicability, calibrate the judge against these observed mistakes, improve schema-error handling, and test narrower withholding. Freeze a new contract and rerun both versions after any shared change. Obtain expert review of the answer key, more scenarios and repeated trials before estimating real-world reliability. No time savings, production failure rate or competitive superiority was measured.

The five synthetic cases, one trial and shared app/judge model limit generalization. The workshop's 576-run reference is not this project's dataset or result. No ARIA challenge or Reports publication is claimed. The student still needs to review the findings and record the [3–5 minute walkthrough](VIDEO_WALKTHROUGH.md).

</details>
