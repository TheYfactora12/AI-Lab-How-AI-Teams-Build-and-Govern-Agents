# Bank AI Vendor Risk Assessment: Scope and Evidence Review

An Evaluation Builder certificate project reviewing a fictional bank's proposed internal AI policy assistant. The assessment agent identifies applicable risks, distinguishes assertions from evidence and produces a draft for human review.

## Start here

**Condensed recording notes:** use the [one-page recording cheat sheet](RECORDING_CHEAT_SHEET.md) for seven links, timing, what to point at, and what to say.

**Recording the project:** open the [GitHub recording guide](GITHUB_RECORDING_GUIDE.md). It gives the exact tab order, what to click, what each screen proves, what to say, and troubleshooting steps.

**Current evidence:** [contract 1.4 comparison](CURRENT_COMPARISON.md) and [V2 correction record](V2_CORRECTION_RECORD.md). Earlier comparisons and stress failures are preserved as historical evidence and are labeled in their files.

**Course alignment:** [certificate requirements map](CERTIFICATE_ALIGNMENT.md). Public-document intake and the broader routing matrix are supporting extensions, not completed public-vendor evaluations.

## Current project status

The current result is **V1: 3 passes and 2 blocks; V2: 3 passes, 1 block and 1 review**. V2 contains C03's unsupported scope and citation decisions. Its C05 generation failed schema validation and was safely withheld. C02 readiness classification remains unresolved. Every client-facing assessment requires human review.

All vendor documents and test records are synthetic. Claims about vendor test results are scenario inputs, not real experiments. Our real Weave traces record the assessment agent's work on those inputs.

## What exists

- Five versioned synthetic cases and a frozen evaluation contract.
- Two model-powered versions differing only by an evidence gate.
- Two independent exact scorers, a live three-criterion judge and 23 current assessment regression tests.
- Completed native Weave evaluations, unedited outputs, receipts and interpretation.
- Notes, references, ownership policy and an own-voice recording outline.

The run snapshots, source fingerprints and interpretation are committed for later review. These results do not establish production readiness. Student review and video recording/upload remain outstanding.

## Open the saved evaluation later

Open the [current GitHub Actions run](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33972108376) or the direct V1/V2 Weave links in the current comparison. Unedited contract 1.4 results are committed in evaluation_snapshots/contract-1.4/. Earlier runs remain separately preserved as historical evidence.

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

The technical comparison, documentation and recording guide are prepared. The student still needs to inspect the selected Weave traces, review the answer-key judgments, rehearse, record a 3–5 minute walkthrough in their own voice, and upload it through the course interface.
