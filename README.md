# Bank AI Vendor Risk Assessment: Scope and Evidence Review

An Evaluation Builder certificate project reviewing a fictional bank's proposed internal AI policy assistant. The assessment agent identifies applicable risks, distinguishes assertions from evidence and produces a draft for human review.

## Review these first

Start with [the saved review package](REVIEW_START_HERE.md) for direct Weave links, the actual V1 output, and observations to discuss.

The [project record and reference index](docs/PROJECT_RECORD.md) collects the decision history, setup notes, source references, GitHub workflow history and Weave links. [Class notes](docs/CLASS_NOTES.md) preserve the supplied image and submission requirements.

1. [Project brief](PROJECT_BRIEF.md): problem, outcome, scope and completion checklist.
2. [Use-case profile](USE_CASE_PROFILE.md): fictional bank, vendor, users and operating boundaries.
3. [Assessment catalog](ASSESSMENT_CATALOG.md): ten requirements across seven risk areas and five cases.
4. [Expected findings](data/expected_findings.json): draft answer key for human review.
5. [V2 plan](V2_CHANGE_PLAN.md): deeper evidence gate as one controlled change.

All vendor documents and test records are synthetic. Claims about vendor test results are scenario inputs, not real experiments. Our real Weave traces record the assessment agent's work on those inputs.

## What exists

- Five versioned input packets and separately stored expected findings.
- A model-powered V1 with a common structured output schema.
- Two independent deterministic scorers and pass/fail/unknown calibration tests.
- A manual workflow to publish the dataset and optionally generate one C01 draft. The first dataset publication and live C01 sample succeeded; the original output is saved in review_snapshots/.

The live judge, V2 gate and full V1/V2 evaluation comparison are not implemented yet. A single sample is not a full evaluation. The evaluation contract and expected findings still need review.

## Open the saved run later

Go to [GitHub Actions](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions), select **Publish review package**, and open the latest completed run. Its summary contains the versioned dataset reference and sample trace link. Download the **review-package** artifact for the receipt, scores and model-generated JSON.

The sample is in Weave **Calls/Traces**, not the Agents sessions view. The dataset is in Weave's dataset/object views. It is not yet a V1/V2 evaluation run.

Workflow artifacts are retained for 90 days. The dataset and trace are separately stored in the W&B project, subject to that account's retention settings. Save downloaded artifacts for longer-term review.

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
