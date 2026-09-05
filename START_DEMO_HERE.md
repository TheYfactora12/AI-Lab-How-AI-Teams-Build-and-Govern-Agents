# Your demonstration handoff

For the shortest seven-tab route and talking points, use the [recording cheat sheet](RECORDING_CHEAT_SHEET.md).

For exact GitHub clicks, tab order, screen meanings and troubleshooting, use the [GitHub recording guide](GITHUB_RECORDING_GUIDE.md). This page is the shorter readiness checklist.

The corrected synthetic V1/V2 experiment (contract 1.2) and its evidence package are ready to review and display with their documented limitations. This does not certify that every acceptance behavior passes. The expanded risk-rating/routing system and public-document assessment are not completed model evaluations.

## Open these tabs before recording

1. [Current comparison](CURRENT_COMPARISON.md): your primary results and evidence guide.
2. [Use-case profile](USE_CASE_PROFILE.md): explain who the assistant helps and what it reviews.
3. [Five-case dataset in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs): show the repeatable test situations.
4. [V1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06d7e-b22d-7497-a050-15150061f01b): find C03's finding and scorer reason.
5. [V2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06d7f-274c-7f26-8385-6c4dabf64fbd): find C03's gate rejection and withheld output.
6. [Comparison report](CURRENT_COMPARISON.md): explain results and the mistakes that graders missed.
7. [Operating policy](OPERATING_POLICY.md): explain automatic drafting, human review and blocked release.

If a private Weave link shows a login/404 page, sign in with the account that has access to this project. Do not change sharing permissions. The [V1](evaluation_snapshots/contract-1.2/v1-rows.json) and [V2](evaluation_snapshots/contract-1.2/v2-rows.json) snapshots preserve the results if you need to find the case first. Search for C03, SEC-01 and gate_record. A saved JSON result is a fallback artifact, not a substitute for personally inspecting the required Weave trace.

## What is finished on the engineering side

- Actual V1/V2 runs, frozen contract, original outputs and receipts are saved.
- The comparison explains the targeted improvement without claiming an overall gain.
- Source code, dataset, rubric, calibration evidence and operating policy are linked.
- Public-document intake has a separately verified trace and clearly stated limits.
- The full walkthrough and recording outline are written.
- Documentation link targets and stored result counts have been checked.

No new model runs or grading changes were made just to improve the presentation. The documentation pull request did not have configured automatic PR checks; local documentation and artifact checks are reported separately from the earlier successful Actions runs.

## Your remaining work

- [ ] Read the expected findings and confirm or challenge the judgment calls. We have not claimed independent expert validation.
- [ ] Open the dataset, V1 and V2 links in your signed-in browser.
- [ ] Locate C03 in both current runs; inspect its V1 exact failure, V2 gate rejection, and one judge call. Read C02 and C05's remaining limitations too.
- [ ] Explain the C03 scope failure in your own words: unknown does not mean no; show the corrected gate withholding it.
- [ ] Explain that three automated passes do not mean three human-validated assessments; C02 still has a readiness-state mismatch that the graders missed.
- [ ] Personalize the [video outline](VIDEO_WALKTHROUGH.md) with your motivation and interpretation.
- [ ] Rehearse for 3–5 minutes with readable text and clear audio.
- [ ] Record in your own voice, show the deliverable, play it back and upload through the course interface.

## Four-minute route

| Time | Display | Main point |
| --- | --- | --- |
| 0:00–0:40 | Use-case profile | A consultant needs supported, scoped evidence review |
| 0:40–1:20 | Dataset and rubric | Five cases and explicit definitions of good behavior |
| 1:20–2:20 | V1/V2 C03 | Locate the failure, then show the gate's containment |
| 2:20–3:20 | Comparison report | Same overall counts, plus scope and judge failures |
| 3:20–4:00 | Operating policy | Human review stays mandatory; next evidence is specified |

The public-document intake is optional backup material for this recording. Keep the main story focused on the completed five-case comparison.

## Accurate closing statement

“V2 caught the targeted unknown-scope error, but the evaluation still exposed readiness-state and judge limitations. I would keep this assistant limited to draft preparation with human review, and improve the evaluation before expanding automation.”

Use this as a factual starting point, not a claim that the project is approved for bank deployment or guaranteed to receive a certificate. The [acceptance map](CERTIFICATE_ALIGNMENT.md) retains the unresolved gaps.
