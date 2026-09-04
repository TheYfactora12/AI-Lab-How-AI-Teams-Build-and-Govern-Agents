# Project record: notes, decisions, references and links

This index records the substantive project context supplied or developed in our working conversation. It is a curated record, not a verbatim transcript. Credential values and credential-bearing filenames are excluded.

## Current project

The user reaffirmed that the official certificate repository is the build specification. [Certificate alignment](../CERTIFICATE_ALIGNMENT.md) maps required artifacts, distinguishes supporting extensions, and records unresolved behavior/coverage gaps. Do not treat implemented infrastructure as proof that all acceptance behavior passes.

Public-source extension: [intake and traceability guide](../PUBLIC_DOCUMENT_REVIEW.md), [registry](../data/public_sources.json), and [frozen download manifest](../data/public_source_manifest.json). Two public SOC 3 PDFs and one vendor AI data-use page were collected. This extension verifies provenance and does not replace the completed synthetic comparison or claim real-vendor risk ratings.

Kevin challenged the initial evaluation's coverage: the workflow should measure task-level automation versus human review across application risk and evidence conditions. [Automation routing design](../AUTOMATION_ROUTING_DESIGN.md) records the clarification, 15 scenario families, proposed metrics and weighting principles. It is a next-experiment design; existing V1/V2 results are preserved, and no broader routing results are claimed.

**Bank AI Vendor Risk Assessment: Scope and Evidence Review** is an Evaluation Builder certificate project. It assesses the scope and evidence needs for a fictional bank's internal AI policy assistant. The user approved the concept and the use-case-dependent approach.

- [GitHub repository](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents)
- [Start reviewing the saved work](../REVIEW_START_HERE.md)
- [W&B project overview](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/overview)
- [Weave project](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave)

The live judge, V2 gate and five-case controlled comparison are complete. Both versions received three automated passes and two blocks; inspection uncovered scope and judge errors. See the [comparison report](../COMPARISON_REPORT.md), [evaluation design](../EVALUATION_DESIGN.md), [policy](../OPERATING_POLICY.md), and [video outline](../VIDEO_WALKTHROUGH.md). Student review and video submission remain pending. Earlier progress entries below are historical.

## Project document and implementation map

| Artifact | Purpose |
| --- | --- |
| [Project brief](../PROJECT_BRIEF.md) | Objective, risk, scope, operating proposal and completion checklist |
| [Use-case profile](../USE_CASE_PROFILE.md) | Fictional bank/vendor, users, data access, authority and reassessment triggers |
| [Assessment catalog guide](../ASSESSMENT_CATALOG.md) | Ten requirements across seven areas, plus case descriptions |
| [Catalog JSON](../data/assessment_catalog.json) | Versioned requirement identifiers, applicability rules, evidence needs and owners |
| [Five input packets](../data/cases.jsonl) | Standalone synthetic case inputs and provenance |
| [Expected findings](../data/expected_findings.json) | AI-assisted answer key, drafted before outputs and pending user review |
| [Dataset manifest](../data/manifest.json) | File fingerprints and input/answer separation contract |
| [Fixture generator](../scripts/build_design_assets.py) | Reproduce the design assets without model calls |
| [V2 change plan](../V2_CHANGE_PLAN.md) | Single deeper evidence gate, fixed comparison conditions and limitations |
| [V1 implementation](../bank_review/app.py) | Model-powered assessor and traced internal calls |
| [Output schema](../bank_review/schema.py) | Structured scope, findings, citations, questions and review state |
| [Deterministic scorers](../bank_review/scorers.py) | Reference integrity and evidence-status/routing checks |
| [Scorer calibration tests](../tests/test_scorers.py) | Ten tests, including pass/fail/unknown, wrong identity, stale dates and timeouts |
| [Publication script](../bank_review/publish.py) | Publish/read back the dataset and optionally create one V1 sample |
| [Pinned direct dependencies](../requirements.txt) | Versions used by the review workflow |
| [Original V1 sample](../review_snapshots/v1-C01.json) | Actual unedited C01 output and scores |
| [Publication receipt](../review_snapshots/publication.json) | Exact code SHA, dataset reference, hashes and run status |
| [Class notes and submission requirements](CLASS_NOTES.md) | Workshop takeaways, original image and assignment context |
| [Optional Agents SDK guide](AGENTS_SDK_REFERENCE.md) | User-supplied Agents-view integration example; not adopted or executed |

The source manifest describes the design's pre-publication state. It is preserved inside the receipt for provenance. The receipt's top-level publication and sample fields record the subsequent successful run; the historical manifest status is not the current publication status.

## Decision history

| Decision | Outcome and reason |
| --- | --- |
| Initial suggested use case | Refund recommendation was proposed, then superseded by the user's banking security consulting idea |
| Track | Evaluation Builder, supported by GitHub Actions and Weave |
| Initial checklist | The user challenged a fixed three-control approach as too narrow for AI vendor risk assessment |
| Revised assessment approach | Determine which requirements apply from intended use; cover use/impact, privacy, security, quality, fairness/accessibility, human oversight and vendor governance |
| First bounded use case | Internal employee policy assistant; fictional Harbor Glen Community Bank and CedarBridge AI PolicyDesk |
| Evidence discipline | Distinguish vendor assertions, documented support and limited observed test records; fictional test records remain labeled synthetic |
| Product ambition | A credible first consulting workflow; no evidence supports a top-1% market claim or validated demand |
| Test cases | Normal, absent role-isolation test, unclear scope, retrieval timeout and contradictory training statements |
| V2 direction | One post-generation evidence-validation gate; do not bundle unrelated model, prompt or retrieval changes |
| Baseline preservation | Save actual V1 output unchanged and keep observations separate from measured scores |
| Review sequence | Review expected findings and V1 output before freezing the rubric/contract and running the full comparison |

Case expectations are not confirmed user judgments merely because the overall project direction was approved. All subsequent evaluation claims must identify whether they are design expectations, local test results, model outputs or human observations.

## Weave links

- [Original synthetic hello trace](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06a53-9e5b-758c-b799-514f7576fbfb): authentication/project-write setup check only.
- [Published five-case dataset, exact version](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs).
- [Actual V1 C01 assessment trace](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06a6e-a2aa-7fcf-aaa4-51c2c8cfc45f).
- [Agents page originally visited](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/agents): this project currently uses function Calls/Traces, so an empty agent-session view is not evidence of failed publication.

Dataset reference:

```text
weave:///kevinmedeiros-masterclass/ai-lab-agent-governance/object/bank-vendor-scope-five-v1:Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs
```

The actual sample uses `OpenPipe/Qwen3-14B-Instruct`, temperature 0, through W&B Serverless Inference. The OpenAI Python SDK is used as an API client for that endpoint, not as evidence that an OpenAI-hosted model was called.

## GitHub workflow history

| Workflow run | Outcome | Meaning |
| --- | --- | --- |
| [Authentication check](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33830702347) | Success | W&B accepted secret W_B |
| [First trace attempt](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33830847356) | Failed | Organization was mistakenly used as project entity |
| [Corrected trace](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33830969912) | Success | Correct team/project destination; trace saved/read back |
| [Initial review-package attempt](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33832753534) | Partial, workflow failed | Dataset published/read back; sample stopped on missing self binding before inference |
| [Corrected review package](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33832814085) | Success | Ten calibration tests, dataset readback, one actual V1 sample and artifact saved |

Workflow definitions:

- [Verify W&B authentication](../.github/workflows/verify-wandb.yml)
- [Log first Weave trace](../.github/workflows/log-weave-trace.yml)
- [Publish review package](../.github/workflows/publish-review-package.yml)
- [All Actions runs](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions)

Code provenance:

- [Initial review implementation](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/commit/6c78913)
- [Exact code used for successful V1 sample](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/commit/688f7cd48e49e5efa0049782ee105121256018e2)
- [Saved baseline and review observations](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/commit/5af6cf8)

## Setup notes

- Correct project entity: `kevinmedeiros-masterclass`. The organization name ending in `-org` was an earlier configuration mistake and must not be used as the project entity.
- GitHub Actions secret name: `W_B`, mapped to `WANDB_API_KEY`. Secret values cannot be retrieved from GitHub for local login.
- Local `.venv` installation and imports succeeded. Local `wandb login` was attempted but did not establish authentication. Live work subsequently used GitHub Actions.
- [Repository secret settings](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/settings/secrets/actions) require repository permissions.
- A key was exposed during initial setup; revocation/replacement was advised. The later stored key authenticated successfully, but that does not independently verify revocation of the earlier key. No credential value is retained in project documentation.
- Reports and ARIA access have not been independently verified.
- Workflow artifacts are configured for 90-day retention. Original sample and publication receipt are additionally committed to the repository. W&B links require appropriate account access and remain subject to W&B retention settings.

## Official course references

These are living upstream links, not pinned snapshots. The published local dataset is separately fingerprinted.

- [Certificate project overview](https://github.com/LorenzoWandB/PatchPilot-MasterClass/tree/main/certificate-project)
- [Evaluation Builder track](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/TECHNICAL_TRACK.md)
- [Evaluation Designer alternative](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/NON_TECHNICAL_TRACK.md)
- [Evaluation design template](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/EVALUATION_DESIGN_TEMPLATE.md)
- [Completed example](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/EXAMPLE_COMPLETED_EVALUATION.md)
- [Use-case options and custom-project guidance](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/USE_CASE_OPTIONS.md)
- [Glossary](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/GLOSSARY.md)
- [Workshop repository](https://github.com/LorenzoWandB/PatchPilot-MasterClass)

## W&B and SDK references supplied during setup

- [Weave documentation](https://docs.wandb.ai/weave)
- [W&B quickstart and authentication guidance](https://docs.wandb.ai/models/quickstart)
- [W&B authorization](https://wandb.ai/authorize)
- [Hello Trace Colab notebook](https://colab.research.google.com/github/wandb/docs/blob/master/weave/cookbooks/source/Intro_to_Weave_Hello_Trace.ipynb)
- [Notebook source](https://github.com/wandb/docs/blob/master/weave/cookbooks/source/Intro_to_Weave_Hello_Trace.ipynb)
- [wandb.init reference](https://docs.wandb.ai/models/ref/python/functions/init)
- [W&B Public API](https://docs.wandb.ai/models/ref/python/public-api)
- [GitHub Actions secret instructions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)

The user supplied a JSON-QA evaluation example using a Weave model, dataset and exact-answer scorer. It informed the execution pattern, not our banking dataset or results. Its dataset reference was `weave:///wandb/json-qa/object/json-qa:v3`; it was not run for this project. The training accuracy/loss snippets and Public API exports were also reference examples, not experiments performed here. A Weave call ID must not be substituted for a W&B Models run ID.

The user also supplied the OpenAI-hosted variant of that JSON-QA example, using `gpt-4.1-nano`, `openai.OpenAI()` and `OPENAI_API_KEY` ([key-management link supplied](https://platform.openai.com/api-keys)). This is recorded as reference material, not a requested provider migration or an executed test. The controlled bank-review comparison retains the W&B Serverless Inference model and W_B authentication used by the existing baseline.

## Banking and market context consulted

- [Federal Reserve: Third-Party Risk Management guide for community banks](https://www.federalreserve.gov/supervisionreg/srletters/SR2402.htm): context for a consulting workflow, not a claim that our catalog satisfies regulatory obligations.
- [NIST CSF Profiles](https://www.nist.gov/cyberframework/profiles): considered as gap-assessment context; no formal NIST mapping has been implemented.
- [Credo AI vendor compliance](https://www.credo.ai/solutions/vendor-compliance), [ModelOp financial services](https://www.modelop.com/solutions/financial-services), and [Arize](https://arize.com/): vendor descriptions consulted to challenge the idea's novelty. No comparative benchmark or market ranking was conducted.

## Open review items

1. Review the AI-assisted expected findings and resolve normal-case packet-state semantics.
2. Decide how the judge will handle overbroad assurance and applicability rationale quality.
3. Finalize the detailed three-criterion rubric and release-policy contract.
4. Freeze dataset, app/judge parameters, scorer/rubric versions and policy before the full comparison.
5. Implement the V2 evidence gate without obscuring limitations it cannot fix.
6. Run V1 and V2 against the same five cases and record actual case-level outcomes.
7. Complete the final report/operating decision and the user's own-voice video.

Update this index and REVIEW_START_HERE.md when new runs or decisions supersede the current state. Keep historical output snapshots intact.


## Completed comparison: September 4, 2026

The user's pasted OpenAI JSON-QA sample is an alternate integration reference, not a request to replace the project's W&B inference provider. No OpenAI credential was needed. The optional Agents SDK example remains separate.

- Contract: [bank-vendor-eval-v1.1](../evaluation_contract.json); original cases and expected findings unchanged.
- Source commit: e4812fe7267b22b082375ad793aedde62e49dfe8.
- [Final Actions execution](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33885310280): completed with 17 calibration tests and both evaluations.
- [V1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cdf-b7f7-7038-93e0-b60ac9376a11), [V2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06ce0-2c54-769e-b851-93e10e0b2f3e).
- [Final receipt](../evaluation_snapshots/final/receipt.json), [V1 rows](../evaluation_snapshots/final/v1-rows.json), [V2 rows](../evaluation_snapshots/final/v2-rows.json).
- [Earlier failed attempt](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33884926606) remains in evaluation_snapshots/attempt-1. Both versions were rerun after common error handling changed; counts are not pooled.

New implementation: bank_review/gate.py, bank_review/judge.py, bank_review/evaluate.py, scripts/freeze_contract.py, tests/test_gate_and_judge.py, and .github/workflows/evaluate-v1-v2.yml. See JUDGE_RUBRIC.md and the [submission checklist](../SUBMISSION_CHECKLIST.md).

V2 withheld an incorrectly supported role-test claim in C02. Overall verdict counts did not improve. C03 scope errors passed every scorer; C05 had application errors and unsupported judge reasoning. Preserve those failures as evidence for the operating decision. No 576-run project comparison, ARIA review, independent expert validation or video submission is claimed.
