# Certificate scope and acceptance map

The user designated the [official certificate project](https://github.com/LorenzoWandB/PatchPilot-MasterClass/tree/main/certificate-project) as the build specification. Checked September 4, 2026. Use its [Evaluation Builder track](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/TECHNICAL_TRACK.md) and [design template](https://github.com/LorenzoWandB/PatchPilot-MasterClass/blob/main/certificate-project/EVALUATION_DESIGN_TEMPLATE.md) to govern the submission.

Our qualifying original use case is a banking consultant's vendor scope-and-evidence review assistant. The course repository supplies instructions and reference patterns; our own GitHub repository holds the implementation and artifacts.

## Required work and evidence

| Required element | Our artifact | Current assessment |
| --- | --- | --- |
| Defined user, outcome, harm and human oversight | EVALUATION_DESIGN.md, PROJECT_BRIEF.md | Written; student review pending |
| Root operation and meaningful internal calls | bank_review/app.py, Weave evaluation links in COMPARISON_REPORT.md | Implemented; student should inspect the nested trace |
| Five complete versioned cases | data/cases.jsonl, expected findings, evaluation_contract.json | Published and frozen; independent answer-key review remains pending |
| Two exact scorers with pass/fail/unknown calibration | bank_review/scorers.py, tests/test_scorers.py | Implemented and calibrated |
| Live three-criterion judge | bank_review/judge.py, JUDGE_RUBRIC.md | Executed; observed rubric-following errors documented |
| Two model-powered versions with one controlled change | V1 baseline and V2 evidence gate | Executed under the same contract |
| Case-level comparison and operating decision | COMPARISON_REPORT.md, OPERATING_POLICY.md | Written with actual failures and limitations |
| Student's own-voice walkthrough | VIDEO_WALKTHROUGH.md, SUBMISSION_CHECKLIST.md | Outline prepared; recording/upload pending |

## Acceptance gaps must remain visible

Do not mark all behavior requirements satisfied merely because the workflow completed. C03's unsafe inference from unknown scope passed every scorer. C05 failed to produce a valid assessment, and the judge invented reasoning instead of honoring the unavailable-evidence rule. C01's expected review state was not matched. These failures weaken evaluation coverage and are recorded without altering the original results.

The course allows unexpected live judgments; that does not excuse incorrect interpretation or hidden missing-evidence passes. Any remediation must freeze a new contract before rerunning both versions. The old comparison remains an auditable experiment.

## Bound the remaining build

Finish one explainable assessment workflow and its evaluation. Task-level automate/review/block decisions can make the existing human-oversight requirement concrete. A simulation risk rubric must support this scope and stay distinguishable from model confidence and real vendor acceptance.

Public SOC-document intake and its provenance trace are supporting research, not a replacement for the required five-case model evaluation. Preserve original real-vendor source identity. Use fictional or sanitized assessment inputs for the certificate. The 15-family routing matrix is a backlog of possible coverage, not a requirement to build every family before submission.

Do not expand into a general GRC platform or add multiple autonomous agents merely for breadth. Select any next intervention from the observed failures and user's workflow objectives, document one V1/V2 difference, keep evaluation conditions fixed, and report both gains and remaining failures. The final demonstration should follow the official order: use case, implementation/trace, dataset/exact checks, judge, comparison, operating policy.
