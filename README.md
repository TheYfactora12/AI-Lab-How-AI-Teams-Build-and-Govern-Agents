# Bank AI Vendor Risk Assessment: Scope and Evidence Review

An Evaluation Builder certificate project reviewing a fictional bank's proposed internal AI policy assistant. The assessment agent identifies applicable risks, distinguishes assertions from evidence and produces a draft for human review.

## Review these first

Start with the [completed comparison report](COMPARISON_REPORT.md), [evaluation design](EVALUATION_DESIGN.md), [30-day operating rule](OPERATING_POLICY.md), and [video outline](VIDEO_WALKTHROUGH.md). The [submission checklist](SUBMISSION_CHECKLIST.md) covers your remaining review and recording steps. The [original sample](REVIEW_START_HERE.md) is preserved as history.

The [project record and reference index](docs/PROJECT_RECORD.md) collects the decision history, setup notes, source references, GitHub workflow history and Weave links. [Class notes](docs/CLASS_NOTES.md) preserve the supplied image and submission requirements.

1. [Project brief](PROJECT_BRIEF.md): problem, outcome, scope and completion checklist.
2. [Use-case profile](USE_CASE_PROFILE.md): fictional bank, vendor, users and operating boundaries.
3. [Assessment catalog](ASSESSMENT_CATALOG.md): ten requirements across seven risk areas and five cases.
4. [Expected findings](data/expected_findings.json): draft answer key for human review.
5. [V2 plan](V2_CHANGE_PLAN.md): deeper evidence gate as one controlled change.

All vendor documents and test records are synthetic. Claims about vendor test results are scenario inputs, not real experiments. Our real Weave traces record the assessment agent's work on those inputs.

## What exists

- Five versioned synthetic cases and a frozen evaluation contract.
- Two model-powered versions differing only by an evidence gate.
- Two independent exact scorers, a live three-criterion judge and 17 calibration tests.
- Completed native Weave evaluations, unedited outputs, receipts and interpretation.
- Notes, references, ownership policy and an own-voice recording outline.

Both versions received three automated passes and two blocks. V2 caught the C02 test mismatch, but inspection found scope and judge errors. These scores do not establish production readiness. Student review and video recording/upload remain outstanding.

## Open the saved evaluation later

Open the [completed GitHub Actions run](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33885310280) or the direct V1/V2 Weave links in the comparison report. Unedited results are committed in evaluation_snapshots/final/; the failed first attempt is separately retained in evaluation_snapshots/attempt-1/.

The implementation uses Weave Calls/Evaluations, not Agents SDK sessions. Workflow artifacts last 90 days; committed snapshots preserve the review record independently. W&B retention depends on account settings.

## Reproduce locally

Use Python 3.12 or the existing project `.venv`.

```powershell
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m bank_review.publish
# Optional: one hosted model call, after authenticating locally
python -m bank_review.publish --sample
```

The workflow maps GitHub secret `W_B` to `WANDB_API_KEY`. Local runs need their own environment authentication; never put a key in code or a notebook. Publishing alone does not call an inference model. The optional sample uses W&B Serverless Inference and may consume credits. No hidden retries are configured.

Weave project: `kevinmedeiros-masterclass/ai-lab-agent-governance`.

## Review questions

- Does the scope fit the internal-assistant use case?
- Are the expected findings correct, and are any important gaps missing?
- Does each conclusion distinguish a vendor claim, documented support and a limited test result?
- Does the draft expose uncertainty instead of declaring the vendor approved?
- Which failures should the one V2 gate address, and which remain separate limitations?

After review: finalize rubric and contract, implement the live judge and V2 gate, run the same five-row evaluation for both versions, then prepare the 3–5 minute video in the user's own voice.
