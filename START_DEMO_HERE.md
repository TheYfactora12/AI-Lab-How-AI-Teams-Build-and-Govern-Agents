# Your demonstration handoff

The first synthetic V1/V2 experiment and its evidence package are ready to review and display with their documented limitations. This does not certify that every acceptance behavior passes. The expanded risk-rating/routing system and public-document assessment are not completed model evaluations.

## Open these tabs before recording

1. [Full project walkthrough](PROJECT_EVIDENCE_WALKTHROUGH.md): your reference guide.
2. [Use-case profile](USE_CASE_PROFILE.md): explain who the assistant helps and what it reviews.
3. [Five-case dataset in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs): show the repeatable test situations.
4. [V1 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06cdf-b7f7-7038-93e0-b60ac9376a11): find C02's finding and scorer reason.
5. [V2 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06ce0-2c54-769e-b851-93e10e0b2f3e): find C02's gate rejection and withheld output.
6. [Comparison report](COMPARISON_REPORT.md): explain results and the mistakes that graders missed.
7. [Operating policy](OPERATING_POLICY.md): explain automatic drafting, human review and blocked release.

If a private Weave link shows a login/404 page, sign in with the account that has access to this project. Do not change sharing permissions. The [V1](evaluation_snapshots/final/v1-rows.json) and [V2](evaluation_snapshots/final/v2-rows.json) snapshots preserve the results if you need to find the case first. Search for C02, SEC-01 and gate_record. A saved JSON result is a fallback artifact, not a substitute for personally inspecting the required Weave trace.

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
- [ ] Locate C01, C02 and C04; inspect at least one exact scorer and one judge call. Read the C03 and C05 limitations too.
- [ ] Explain the C02 mismatch in your own words: an injection test is not a role-isolation test.
- [ ] Explain that three automated passes do not mean three human-validated assessments; C03 was a missed scope error.
- [ ] Personalize the [video outline](VIDEO_WALKTHROUGH.md) with your motivation and interpretation.
- [ ] Rehearse for 3–5 minutes with readable text and clear audio.
- [ ] Record in your own voice, show the deliverable, play it back and upload through the course interface.

## Four-minute route

| Time | Display | Main point |
| --- | --- | --- |
| 0:00–0:40 | Use-case profile | A consultant needs supported, scoped evidence review |
| 0:40–1:20 | Dataset and rubric | Five cases and explicit definitions of good behavior |
| 1:20–2:20 | V1/V2 C02 | Locate the failure, then show the gate's containment |
| 2:20–3:20 | Comparison report | Same overall counts, plus scope and judge failures |
| 3:20–4:00 | Operating policy | Human review stays mandatory; next evidence is specified |

The public-document intake is optional backup material for this recording. Keep the main story focused on the completed five-case comparison.

## Accurate closing statement

“V2 caught the targeted evidence mismatch, but the evaluation also exposed scope and judge failures. I would keep this assistant limited to draft preparation with human review, and improve the evaluation before expanding automation.”

Use this as a factual starting point, not a claim that the project is approved for bank deployment or guaranteed to receive a certificate. The [acceptance map](CERTIFICATE_ALIGNMENT.md) retains the unresolved gaps.
