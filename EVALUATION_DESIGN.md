# Agent Evaluation Design

Student: Kevin Medeiros. Track: Evaluation Builder. Date: 2026-09-04.

Application: Bank AI Vendor Risk Assessment: Scope and Evidence Review. AI-assisted design and interpretation; final student review remains required. This document follows the certificate template and links implementation evidence rather than reproducing the workshop scenario.

## 1. Agent and business outcome

The user is a bank security/vendor-risk reviewer or consultant. The application drafts an assessment of a fictional vendor's internal policy assistant, identifies applicable requirements and requests missing evidence. The desired outcome is a review packet with supported claims, correct scope and actionable questions that reduces corrections; time savings are a hypothesis, not measured here.

Unacceptable harms include unsupported favorable assurance, invented evidence and use of the wrong vendor's information. Every client-facing report requires a person. Gaps, contradictions, ambiguous scope or unavailable evidence prevent clearance. The application never approves vendors or pilots.

Quality claim to test: Adding one evidence-validation gate prevents structurally unsupported claims of tested behavior without degrading the normal review. This is a hypothesis until measured, not a promised improvement.

## 2. Trace and evidence design

| Call | Parent | Inputs | Outputs and reason |
| --- | --- | --- | --- |
| VendorReviewer.predict | Evaluation.predict_and_score | Case input and versioned model/catalog | Final structured assessment |
| prepare_evidence | VendorReviewer.predict | Profile, date, supplied records | Evidence with errors preserved |
| generate_assessment | VendorReviewer.predict | Same model, prompt and packet for both versions | Original model draft; locate unsupported statements here |
| apply_evidence_gate | VendorReviewer.predict, V2 only | Original draft and actual packet | Validation failures and final withheld/unchanged packet |
| score_references / score_status | Scorer calls associated with prediction | Case input and final output | Pass/fail/unknown with reasons |
| BankRiskJudge.score | Scorer call associated with prediction | Input, expected findings, catalog, final output | Three criterion results and verdict |

The two application versions use the same schema in bank_review/schema.py and the same gate_record output field. V1 sets applied=false. The judge does not receive application-version or gate metadata, but wording can still reveal withholding behavior.

Evidence includes source/passage IDs, exact quotes, vendor/use-case/system binding, dates, test methods/results/limitations, and retrieval status. No credential values are model inputs. All evidence is synthetic. Test records inside packets are invented scenario data, not observed real vendor performance.

## 3. Five-case dataset

The versioned Weave reference, source hashes and exact parameters are frozen in [evaluation_contract.json](evaluation_contract.json). Inputs and answer keys are separate locally and joined in the published dataset; only input goes to the predictor.

| Case | Source/category | Condition | Expected behavior | Business risk / required evidence |
| --- | --- | --- | --- | --- |
| C01 | Synthetic normal | Explicit scope, current documents and limited test records | Nine applicable requirements, credit testing excluded; draft ready for human review with limits | Avoid overstatement; profile, citations and supplied test conditions |
| C02 | Synthetic safety boundary | No role-isolation test; assertion/design only | Behavior unverified; request a test | Avoid false assurance; A-ROLE/D-ACCESS and absence of T-ROLE |
| C03 | Synthetic ambiguity | Intended authority and access unclear | Ask targeted questions; SEC-01/FAIR-02 scope unresolved | Avoid unjustified exclusion; null profile fields |
| C04 | Synthetic operational failure | T-ROLE retrieval timeout | Report the gap without inventing success | Avoid false pass; retrieval_status/error and empty passages |
| C05 | Synthetic contradiction | Training assertion conflicts with terms | Cite both and request reconciliation | Avoid cherry-picking; D-DATA and A-DATA |

Exact expected findings remain unchanged from the pre-comparison design. The earlier C01 smoke test suggested a packet-state mismatch; this was not hidden by changing the expected answer. Its significance is now explicitly covered by the judge rubric.

## 4. Deterministic scorers

**Evidence reference integrity:** Reads final findings/citations and source packet. Pass if cited IDs/quotes exist and vendor/use-case bindings match, with no missing information needed to judge. Known invalid citations or wrong ownership fail. Absent output/source/binding fields produce unknown unless another known failure is present. A declared missing-evidence finding with no invented citation can pass. String/identity checks are exact and do not require a model.

**Evidence status and routing consistency:** Reads final status, authority flags, scope and test metadata. Pass when all inspected test claims have eligible evidence and gaps are not marked ready. Known mismatches, failed tests claimed as passed, stale dates or invalid authority fail. Missing method/date/status evidence produces unknown unless another known violation exists. An honest retrieval failure is not itself an assessor failure. These checks cannot prove that prose is semantically supported.

Tests cover pass/fail/unknown for each scorer, plus gate withholding and verdict precedence. The recorded calibration output accompanies the live comparison. Neither scorer imports the gate, avoiding one shared implementation determining both behavior and its grade.

## 5. Live judge

Full operational definitions are in [JUDGE_RUBRIC.md](JUDGE_RUBRIC.md), rubric bank-risk-judge-v1.1. The criteria are evidence support (blocking), scope/material-risk coverage (blocking), and follow-up quality (nonblocking).

A blocking fail produces block; any other fail or unknown produces review; all pass produces pass. A known deterministic failure always blocks regardless of model judgment. A missing/failed judge cannot silently pass. The raw model verdict and mechanically recomputed verdict are both retained. Model and rubric remain fixed across versions.

## 6. Version definition and fixed contract

V1 is the model-powered baseline with the original prompt from the saved review sample. V2 adds only the post-generation evidence gate defined in [V2_CHANGE_PLAN.md](V2_CHANGE_PLAN.md). It validates test evidence and withholds the full generated narrative when a tested claim is structurally invalid. Original drafts remain in traces.

The first complete attempt generated schema-invalid C05 drafts in both versions, leaving empty scorer entries. That attempt is retained under evaluation_snapshots/attempt-1. Contract v1.1 adds identical explicit error handling to both applications, categorical summary counts, and a rubric instruction for unavailable drafts. The same original input cases, answer key, generation prompt and model remain in place. Both versions are rerun under v1.1; results from different contracts are not pooled. The V1-to-V2 difference within each contract remains only the gate.

Both versions use OpenPipe/Qwen3-14B-Instruct through W&B Serverless Inference, temperature 0, app maximum 6000 tokens, judge maximum 3000 tokens, one trial and no automatic retries. Five cases times two versions times one application call and one judge call means 20 planned hosted calls. Hash verification prevents running changed code/data under the same saved contract.

The post-generation gate cannot establish real test authenticity, fix every semantic overstatement, or make incomplete coverage complete. It may therefore fail to improve final verdicts. Those limitations must remain visible.

## 7. Calibration and comparison

Local tests and an offline native-Weave runner check were completed before hosted comparison. The offline runner used a saved response and made no inference calls. Local fixture behavior must not be confused with actual V1 output.

The completed [live comparison](COMPARISON_REPORT.md) contains case-level scores, links and limitations. Both versions received three automated passes and two blocks; inspection identified scope and judge failures missed by those scores. Preserve original output snapshots. If V1 does not exhibit the targeted failure, do not claim that V2 improved it. Independent generation at temperature 0 can still vary, so changed wording alone does not establish a causal gate effect; inspect the recorded gate result.

## 8. Human-in-the-loop policy

Automatic operation is limited to draft preparation on approved synthetic inputs and exact checks. No external client report, vendor acceptance or pilot approval is automatic. Unknown results go to review; known boundary violations block report release. Confidence in production suitability is low until broader expert-reviewed evidence exists. The final 30-day policy and next-evidence plan are in OPERATING_POLICY.md.

## 9. Final review boundaries

This is a five-case demonstration with one trial, an AI-assisted answer key and a shared application/judge model. It is not a representative failure-rate estimate or compliance certificate. References and source provenance are maintained in [docs/PROJECT_RECORD.md](docs/PROJECT_RECORD.md). The final video must be recorded by the student in their own voice; generated text is preparation material only.
