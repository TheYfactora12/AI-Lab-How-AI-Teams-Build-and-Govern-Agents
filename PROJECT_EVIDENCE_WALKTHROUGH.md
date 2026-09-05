# Project walkthrough: what we built, what happened, and what the evidence means

**Historical first-loop walkthrough.** For the corrected V2 presentation, start with [current comparison](CURRENT_COMPARISON.md), [demonstration handoff](START_DEMO_HERE.md) and [change record](V2_CORRECTION_RECORD.md). The counts and C02 intervention below describe contract 1.1; contract 1.4 demonstrates the expanded C03 scope and citation-boundary fix.

Prepared for Kevin Medeiros. This guide follows the class sequence: **Run → Observe → Curate → Evaluate → Improve → Repeat**. It describes actual saved work and separates it from proposed extensions. The [official assignment](https://github.com/LorenzoWandB/PatchPilot-MasterClass/tree/main/certificate-project) defines the requirements; [our alignment map](CERTIFICATE_ALIGNMENT.md) records remaining acceptance gaps.

## Start here: the project in plain English

We built an AI assistant for a banking security consultant. It reads a fictional vendor's intended-use profile and evidence packet, drafts cited findings, and identifies questions for a person. We evaluate the assistant's assessment quality, not the vendor's real security.

The fictional client is Harbor Glen Community Bank. The fictional vendor is CedarBridge AI, offering PolicyDesk, an internal policy assistant. The real public documents collected later retain their original vendor identities and are a separate intake experiment.

**Question tested:** Does adding an evidence-validation gate prevent structurally unsupported claims of tested behavior?

**Observed answer:** V2 caught a wrong-test mismatch in C02. Its exact status check improved, but both versions still received three automated passes and two blocks. Other mistakes escaped the graders. Every report therefore remains subject to human review.

Read [project brief](PROJECT_BRIEF.md), [use-case profile](USE_CASE_PROFILE.md), and [full comparison](COMPARISON_REPORT.md).

## The six steps at a glance

| Step | What we did | Main evidence |
| --- | --- | --- |
| Run | Generated actual assessments using V1 | [V1 Weave evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cdf-b7f7-7038-93e0-b60ac9376a11) |
| Observe | Inspected outputs and grading reasons | [Unedited V1 case outputs](evaluation_snapshots/final/v1-rows.json) |
| Curate | Defined five repeatable situations with expected findings | [Dataset in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs) |
| Evaluate | Applied two exact scorers and a live three-criterion judge | [Evaluation design](EVALUATION_DESIGN.md), [judge rubric](JUDGE_RUBRIC.md) |
| Improve | Added V2's post-generation evidence gate | [Gate code](bank_review/gate.py), [V2 outputs](evaluation_snapshots/final/v2-rows.json) |
| Repeat | Ran both versions against the same frozen test | [Comparison](COMPARISON_REPORT.md), [operating policy](OPERATING_POLICY.md) |

This is a teaching order, not a claim that cases were invented after observing these final results. The synthetic cases and answer key were designed before the controlled comparison. The failed first attempt and final rerun are preserved separately.

## 1. Run: give the assistant a defined task

**Open:** [use-case profile](USE_CASE_PROFILE.md), [input packets](data/cases.jsonl), and [V1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cdf-b7f7-7038-93e0-b60ac9376a11).

The input contains an assessment date, application profile and evidence records. The profile describes users, data access and authority. Evidence records carry identifiers, source types, passages and test metadata. The response contains scope decisions, findings, citations, questions and a review state.

Both application versions use OpenPipe/Qwen3-14B-Instruct through W&B Inference. The judge also makes live model calls. The workshop slide's statement that only the judge is live describes its prepared workshop demonstration, not this certificate implementation.

**Show:** one case's input and final response. **Say:** “This is the evidence we supplied and the assessment the assistant actually produced.” **Do not claim:** the fictional tests prove a real vendor is secure.

## 2. Observe: inspect how the answer was produced

**Open:** the V1 evaluation above and locate C02 through the case inputs. Expand the prediction and its recorded steps. The [saved V1 JSON](evaluation_snapshots/final/v1-rows.json) is a fallback: search for `C02`, then `SEC-01`.

| Operation name | Plain-English meaning |
| --- | --- |
| VendorReviewer.predict | Produce the case's final assessment |
| prepare_evidence | Prepare the supplied profile and records |
| generate_assessment | Ask the model to draft an assessment |
| apply_evidence_gate | In V2, validate tested claims and withhold an invalid draft |
| score_references | Check cited source identity and quoted passages |
| score_status | Check whether evidence supports the declared test/status fields |
| BankRiskJudge.score | Grade qualitative assessment behavior |

One recorded function execution is a **call**. Related calls form a **trace**. Inputs show what a step received; output shows what it returned. A successful execution is different from an accurate answer. Green execution status does not approve the vendor. A yellow status requires inspecting its details, not guessing its meaning.

**C02 finding:** a role-isolation finding used T-INJECTION, a test for a different requirement. A real citation can still be the wrong evidence. The exact status check caught this; the AI judge passed it.

**Show:** finding, referenced test and scorer reason. **Say:** “The citation exists, but the test does not support this requirement.” Observations in our GitHub report are not claimed to be saved Weave annotations.

## 3. Curate: define repeatable tests and expected behavior

**Open:** [five-case Weave dataset](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs), [expected findings](data/expected_findings.json), and [catalog](ASSESSMENT_CATALOG.md).

| Case | Situation | What good behavior should demonstrate |
| --- | --- | --- |
| C01 | Normal packet | Supported findings with limits and appropriate draft-review state |
| C02 | Role test missing | Recognize missing proof; do not substitute another test |
| C03 | Scope fields unknown | Ask for clarification; do not convert unknown to no |
| C04 | Retrieval timeout | Disclose missing access to evidence; do not invent success |
| C05 | Conflicting statements | Surface both sources and request reconciliation |

The expected findings are AI-assisted design judgments and still need the student's/expert's review. They were not changed to make the observed model outputs pass. The dataset has a fixed version so both applications receive the same test.

**Show:** one row's input and expected behavior. **Say:** “We decide what good behavior means before grading the responses.”

## 4. Evaluate: use exact rules and a qualitative judge

**Open:** [scoring design](EVALUATION_DESIGN.md), [exact scorer implementation](bank_review/scorers.py), [rubric](JUDGE_RUBRIC.md), and [recorded calibration](evaluation_snapshots/final/calibration.txt).

| Grader | Question | Important limit |
| --- | --- | --- |
| Reference integrity | Do the source IDs and quotes exist and match the vendor/use case? | A valid citation does not guarantee a supported conclusion |
| Evidence status/routing | Does a tested claim have appropriate test metadata, and are gaps handled consistently? | It does not independently verify all applicability decisions |
| AI judge | Are evidence support, scope/risk and follow-up quality acceptable? | Its reasoning can be incorrect or inconsistent |

Exact graders return pass, fail or unknown. Judge criteria also have individual statuses; fixed rules turn them into pass, review or block. An exact failure cannot be overridden by a favorable judge. Unknown is not a pass. A correctly disclosed vendor evidence gap can nevertheless pass an evaluation of the assessor's behavior.

Seventeen calibration tests passed for the completed comparison. The later intake extension added six separate tests. Do not describe 23 tests as 23 model assessment cases.

**Show:** C02's exact failure next to the judge's favorable grading. **Say:** “The disagreement shows why we need inspectable exact checks and human judgment.”

## 5. Improve: change one thing in V2

**Open:** [V2 intervention](V2_CHANGE_PLAN.md), [gate implementation](bank_review/gate.py), [V2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06ce0-2c54-769e-b851-93e10e0b2f3e).

V2 adds one check after model generation. For a tested claim, the gate checks source availability, identity, exact quotations, test authority, requirement, version, date, method, limitations and result. It withholds the generated narrative if a claim fails those structural checks. The original draft remains recorded.

On C02, the gate rejected the mismatched test. V2's final output passed the exact evidence-status check, while the combined verdict remained block. Whole-packet withholding also removes other useful findings. It is a limited containment measure, not a full assessment repair.

**Show:** C02's gate_record, rejected requirement and withheld output. **Say:** “This is the actual targeted change and its tradeoff.”

## 6. Repeat: compare and make an operating decision

**Open:** [comparison report](COMPARISON_REPORT.md), [frozen contract](evaluation_contract.json), and [final receipt](evaluation_snapshots/final/receipt.json).

| Case | V1 automated verdict | V2 automated verdict | What inspection adds |
| --- | --- | --- | --- |
| C01 | pass | pass | Both returned needs_evidence rather than expected review readiness |
| C02 | block | block | V2 contained the wrong-test claim; exact status improved |
| C03 | pass | pass | Both made material scope mistakes that graders missed |
| C04 | pass | pass | Both disclosed the retrieval failure and requested evidence |
| C05 | block | block | Both returned application errors; judge reasoning was unsupported |

Three passes and two blocks in each version is the stored automated result, not a human certification of three correct assessments. In particular, C03 must not be accepted on that pass. C05 had no valid draft, so the judge's invented substantive criticism is not evidence that the agent made that claim in its final output.

The first attempt had incomplete C05 scoring. Shared error handling was added to both versions and both were rerun. [Attempt 1](evaluation_snapshots/attempt-1/SUMMARY.md) remains separate from the final comparison; we did not mix contracts or change the answer key. No overall improvement, measured time savings or production reliability is claimed.

**Show:** result table and the [30-day policy](OPERATING_POLICY.md). **Say:** “We retain the gate, keep every report under human review, and prioritize scope and judge failures before expanding.” The 30-day rule is a proposal, not a pilot already started.

## Automation, review and blocking

| Decision | Current bounded policy |
| --- | --- |
| Automate | Synthetic packet preparation, recorded checks and draft generation |
| Human review | Assessment conclusions, missing evidence, uncertain scope and every client-facing report |
| Block | Release of reports with known boundary failures; inspect disputed judge blocks |
| Revert | Stop the workflow and use manual review when a material failure requires it |

The consultant owns interpretation, the bank reviewer owns risk acceptance, and the technical owner can stop the workflow. Names and approval records are not yet assigned for any real deployment. [Broader routing design](AUTOMATION_ROUTING_DESIGN.md) is a proposed next experiment; no calibrated numerical risk score or model-confidence cutoff has been validated.

## How GitHub and Weave connect

| Evidence | What it establishes |
| --- | --- |
| [Executed source commit](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/tree/e4812fe7267b22b082375ad793aedde62e49dfe8) | The application and evaluator code used for the final comparison |
| [Successful Actions run](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33885310280) | Execution and calibration history |
| [Frozen contract](evaluation_contract.json) | Dataset, model/settings, scorer/rubric versions and file fingerprints |
| [Final receipt](evaluation_snapshots/final/receipt.json) | Connects the source commit, contract and exact Weave run IDs |
| [V1 snapshot](evaluation_snapshots/final/v1-rows.json) / [V2 snapshot](evaluation_snapshots/final/v2-rows.json) | Original case outputs and score reasons preserved for review |

`git_commit` identifies a code revision. `sha256` is a file fingerprint used to detect changed bytes. Neither is a risk score. N/A in a metadata column does not itself indicate an assessment failure.

## Public-document intake: a separate supporting demonstration

**Open:** [intake guide and source links](PUBLIC_DOCUMENT_REVIEW.md), [intake trace](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cee-1c4a-79f9-8b7f-cc01ad29be0a), and [receipt](intake_snapshots/first/receipt.json).

We collected Cloudflare's historical SOC 3, AWS's 2024–2025 SOC 3 and Cloudflare AI data-use documentation. All three fingerprints matched in the live verification. Metadata is versioned in Weave; original files are kept locally. The run made zero model calls. It proves a source-tracking foundation, not a real-vendor risk assessment or a public-document V1/V2 comparison.

Current limit: downloads/parsing happen before the traced verification batch; those failures appear in GitHub logs rather than nested download calls in Weave. Include this extension only if time permits after the main certificate story.

## What to click and capture

Stay signed in to W&B. Open the direct run links rather than searching generated names such as rich-oak. Locate cases through their input case information; child calls may require expanding the trace tree or opening the call's full view. Labels vary, so these instructions identify the content to find rather than promise exact button positions. The provided screen showed Traces on the left and Call, Code, Feedback, Scores and Summary tabs on the right.

If the page shows 404 with a login prompt, check the signed-in account/project access. Do not make the project public to solve a navigation issue. If the interface is confusing, use the linked JSON snapshots to identify the case, then match the evidence in Weave. GitHub search within a file can locate C02, SEC-01, gate_record or final_verdict.

Capture: purpose/profile; five-case dataset; V1 C02 finding and scorer reason; one judge result; V2 C02 rejection; comparison table; human-review policy. Hide credentials and unrelated browser content. A screenshot is presentation support; the linked trace and saved results are the underlying evidence.

## Recording and completion

Use [VIDEO_WALKTHROUGH.md](VIDEO_WALKTHROUGH.md) for a roughly four-minute narration: purpose (40 seconds), cases/checks (45), V1 failure and V2 intervention (60), results/limitations (60), operating decision (35). Personalize the words and explain your own judgment. The video must use your own voice.

Before submission, review the answer key, inspect the chosen traces, explain the observed failures honestly, and use [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md). The technical artifacts exist, but unresolved behavior/coverage gaps remain. No ARIA challenge, 576-run project result, real-vendor clearance, production approval or recorded/uploaded video is claimed.
