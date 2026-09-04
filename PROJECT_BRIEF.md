# Bank AI Vendor Risk Assessment: Scope and Evidence Review

Status: Direction approved by the user; detailed design and implementation pending.
Track: Evaluation Builder.

## Locked project decision

Build an assessment assistant that determines which risk areas apply to a bank's proposed internal AI assistant, explains the required evidence, and identifies evidence gaps for a human reviewer. Evaluate the quality of this assessment assistant in Weave. This supersedes the earlier fixed three-control checklist proposal.

First deliverable: A cited assessment scope and evidence-gap review packet for one fictional vendor and one fictional bank use case. The project will distinguish vendor claims, documented evidence, and observed test results. It will never treat a policy statement as proof of deployed system behavior.

Working scenario defined in [USE_CASE_PROFILE.md](USE_CASE_PROFILE.md): Fictional Harbor Glen Community Bank proposes a read-only internal policy assistant from fictional CedarBridge AI. The profile specifies users, data access, decision authority, human owners, and scope-change triggers. These are design assumptions for the simulation, not verified vendor capabilities or an approved deployment.

## Problem and audience

Help a bank security or third-party risk reviewer determine the assessment scope and evidence needs for an AI software vendor in a specific intended use. Initial market assumption: U.S. community banks. Validate this assumption with prospective clients before treating it as a commercial finding.

Reviewing questionnaires and policies takes time, and favorable vendor claims can conceal missing or contradictory evidence. The agent will draft a cited assessment for a human consultant to review. It will not approve vendors, certify compliance, or change bank systems.

## Initial scope

Use fictional vendor documents, a fictional bank use-case profile, and a versioned assessment catalog. Inputs include a vendor identifier, intended use, affected users, data access, tools, decision authority, questionnaire, policies, supporting evidence, and assessment date.

Candidate assessment areas are use and impact; data and privacy; security; model quality; fairness where relevant; human oversight; and vendor governance, continuity, and exit. For each area, explain applicability or why more information is needed. Do not impose every requirement universally or invent regulatory obligations. Assessment breadth is use-case dependent; the certificate implementation remains bounded to this one scenario.

Outputs:
- Applicable assessment areas and requirements with use-case-based reasons.
- Claims with document and passage citations and explicit evidence type: vendor assertion, documented support, or observed test result.
- Missing, outdated, or contradictory evidence.
- Follow-up questions and suggested remediation.
- Tests still needed to verify behavior that documents cannot establish.
- A draft review packet with owners, operating restrictions, reassessment triggers, and clear reasons for human review or blocking release.

Example: A questionnaire says customer data is never used for training, while the policy permits training unless the customer opts out. Flag the contradiction and cite both passages.

## Why AI and where human judgment belongs

AI connects use-case characteristics to applicable assessment areas, compares differently worded documents, identifies contradictions, and drafts understandable findings. Deterministic checks verify exact requirements such as vendor identity and evidence references. The consultant defines the assessment catalog and expected case outcomes, checks findings, and approves every client-facing assessment. Document text is evidence, never authority to change the agent's instructions.

## Success and unacceptable harm

Measure assessment-scope accuracy against case expectations drafted before model outputs, supported-claim rate, detection of seeded material gaps, correct escalation for missing evidence, and reviewer correction burden. Expectations are AI-assisted and pending user review, not independent expert ground truth. Set numerical thresholds before evaluating V1 and V2. Measure review time only if an actual timed comparison is performed. Five cases establish a certificate demonstration, not market leadership or production readiness.

Unacceptable harm: A favorable assessment misrepresents a material security risk, invents evidence, or uses another vendor's confidential information.

## Trace design

Proposed root operation: `assess_vendor_use_case`.

Proposed internal operations:
1. `determine_assessment_scope`: map the use-case profile to relevant catalog requirements, recording rationale and uncertainty.
2. `retrieve_vendor_evidence`: select documents for the requested vendor and applicable requirements.
3. `check_evidence_requirements`: verify identity, required fields, retrieval status, evidence type, and freshness under explicitly defined rules.
4. `draft_review_packet`: produce scope, cited claims, gaps, questions, required tests, and routing recommendations.

Record fictional inputs, document IDs and versions, relevant excerpts, retrieval failures, rule outcomes, model and prompt versions, and final output. Never record credentials or real confidential banking/vendor data in this project.

## Five-case dataset plan

All cases will use declared synthetic sources. Expand each into exact inputs, expected behavior, business risk, and required evidence before running evaluations.

| Case | Condition | Expected behavior |
| --- | --- | --- |
| Normal | Clear internal-assistant use case with current, consistent evidence | Select the expected assessment scope and produce a supported draft for human approval |
| Safety boundary | Vendor asserts access isolation but no behavioral test supports it | Preserve the assertion as a claim; identify isolation testing needed; do not label behavior verified |
| Ambiguous input | Intended data access or decision authority is unspecified | Ask targeted questions and mark affected scope decisions unresolved |
| Operational failure | Document retrieval fails | Preserve failure evidence; do not treat failure as a clean assessment |
| Contradictory evidence | Questionnaire and policy disagree | Cite both statements and escalate the unresolved contradiction |

## Evaluation contract to complete

Two proposed deterministic scorers to finalize:
- Evidence reference integrity: verify cited document IDs and passages exist and belong to the requested vendor and use case.
- Evidence-status and routing consistency: verify claims marked behaviorally tested reference an actual supplied test record, and missing or failed evidence is not labeled verified or cleared for release.

Define exact `pass`, `fail`, and `unknown` conditions and inspectable fields for each scorer. Missing evidence must not silently pass. Distinguish a correct agent response to missing vendor evidence from a scorer being unable to assess the agent because trace evidence is missing. Citation existence alone does not establish that a passage supports a conclusion.

Three AI-judge criteria:
- Conclusions are supported by cited evidence (blocking).
- Assessment scope fits the intended use and covers material risks and contradictions.
- Follow-up questions are specific and actionable.

Specify per-criterion pass/fail/unknown rules, evidence-based reasons, and an overall pass/review/block verdict. Separate evaluation verdicts from vendor acceptance decisions.

## V1 and V2 comparison

V1 weakness to test: The draft can present vendor assertions or policy statements as verified behavior despite insufficient supporting evidence.

Single targeted V2 change: Add an evidence-validation gate checking supplied test provenance, availability, identity, version, scope, dates and result before allowing a behavioral-verification claim. Keep scope-selection logic unchanged. See [V2_CHANGE_PLAN.md](V2_CHANGE_PLAN.md) for the deeper fix, independent scoring plan and limits.

Keep dataset, scorers, rubric, judge model, and other application settings fixed. Include normal, unsafe, and insufficient-evidence outputs. Store actual results with trace links; do not present predictions or workshop reference results as measured project outcomes.

## Proposed 30-day operating policy

This is a proposed policy, not an approved deployment or evidence of safety.

- Allow automatic drafting on authorized fictional or appropriately approved data.
- Require human review for uncertainty, contradictions, missing evidence, and every client-facing report.
- Block report release for unsupported material conclusions or evidence belonging to the wrong vendor.
- Consultant owns assessment quality; bank reviewer owns vendor acceptance; implementation owner handles access and tracing.
- Pause the workflow and revert to manual review if a material unsupported conclusion or cross-vendor evidence use is found.
- Review observed failures, reviewer corrections, and case coverage after 30 days before proposing broader scope.

## Existing setup

- GitHub: https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents
- W&B project: `kevinmedeiros-masterclass/ai-lab-agent-governance`
- GitHub Actions secret name: `W_B`; mapped to `WANDB_API_KEY`. No secret value belongs in this file.
- Local environment: `.venv`, with wandb 0.29.0 and weave 0.53.8; imports verified.
- Authentication succeeded in GitHub Actions.
- Synthetic setup trace saved and read back: https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06a53-9e5b-758c-b799-514f7576fbfb
- The setup trace is not a model call or evaluation. V1 is implemented in bank_review/app.py; live review-package status is recorded in GitHub Actions. No full evaluation results exist yet.
- Reports and ARIA access remain unverified.

## Certificate completion checklist

- [x] Select an original use case and project track.
- [x] Verify W&B authentication and basic Weave tracing.
- [ ] Complete the official evaluation design template.
- [x] Define the internal-assistant use-case profile and operating boundaries.
- [x] Create the versioned assessment catalog and fictional vendor evidence packets; see [ASSESSMENT_CATALOG.md](ASSESSMENT_CATALOG.md).
- [x] Draft five cases and expected outcomes in data/; model runs have not occurred.
- [ ] Review expected findings with the user and freeze the evaluation contract.
- [x] Implement traced V1 using W&B Serverless Inference with OpenPipe/Qwen3-14B-Instruct; live access checked by the review-package workflow.
- [x] Implement two deterministic scorers; ten local calibration tests pass.
- [ ] Finalize and implement the three-criterion AI judge.
- [ ] Run V1 and V2 under the same evaluation contract.
- [ ] Inspect failures and record actual results with evidence links.
- [ ] Finalize the human-in-the-loop policy based on results.
- [ ] Prepare a portfolio-ready assessment and evaluation summary.
- [ ] Record and upload a 3–5 minute walkthrough in the user's own voice, showing the final deliverable.

## References

- Certificate requirements: https://github.com/LorenzoWandB/PatchPilot-MasterClass/tree/main/certificate-project
- Weave documentation: https://docs.wandb.ai/weave
- Banking context: https://www.federalreserve.gov/supervisionreg/srletters/SR2402.htm

The banking guidance informs the scenario; this prototype does not establish regulatory compliance. Commercial demand, competitive advantage, and time savings remain unvalidated hypotheses. Future authorized behavioral testing of the vendor system is distinct from the Weave evaluations of our assessment assistant.
