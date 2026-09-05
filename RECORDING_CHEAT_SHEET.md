# Recording cheat sheet

Use this beside your screen while recording. The links are in presentation order. Your main message is: **V2 caught the targeted unknown-scope error, but remaining readiness and judge limitations require human review.**

## Before recording

- Sign in to [GitHub](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents) and W&B.
- Open the seven links below in separate tabs.
- Confirm both private Weave links load.
- Increase browser zoom so the text is readable.
- Hide account settings, API keys, email, notifications, and unrelated tabs.

## Seven-tab presentation

| Time | Link | Point to this | Talking point |
| --- | --- | --- | --- |
| 0:00–0:20 | [1. README](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/README.md) | Title and **Current project status** | “I selected the Evaluation Builder track and built a Python AI assistant for banking vendor-risk reviews.” |
| 0:20–0:50 | [2. Use-case profile](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/USE_CASE_PROFILE.md) | **The two systems**, **Business problem**, and **Permitted output** | “The fictional vendor provides an internal policy assistant. My agent reviews its intended use and evidence for a consultant. It drafts findings but cannot approve the vendor.” |
| 0:50–1:25 | [3. Evaluation design](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/EVALUATION_DESIGN.md) | **Five-case dataset**, then scorer/judge sections | “Five cases test normal evidence, a missing test, unknown scope, retrieval failure, and conflicting sources. Exact rules check citations and status; an AI judge reviews support, scope, and follow-up quality.” |
| 1:25–1:55 | [4. Current comparison](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/CURRENT_COMPARISON.md) | **What matters** table and C03 row | “Both versions received three automated passes and two blocks with zero application errors. Equal totals hide an important case-level change.” |
| 1:55–2:30 | [5. V1 C03 in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06d7e-b22d-7497-a050-15150061f01b) | C03 input fields `restricted_documents=null` and `credit_decisions=null`; `score_status` reason | “Null means the bank has not answered the question. V1 turned unknown information into scope conclusions. The corrected exact scorer blocks that behavior.” |
| 2:30–3:15 | [6. V2 C03 in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a06d7f-274c-7f26-8385-6c4dabf64fbd) | `apply_evidence_gate`, `gate_record`, two rejected requirements, `needs_clarification`, and `withheld` | “V2 adds a validation gate after generation. It catches both unsupported scope decisions, preserves uncertainty, withholds the draft, and requests human clarification.” |
| 3:15–3:50 | [7. Operating policy](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/OPERATING_POLICY.md) | **Routing rules** and **Team ownership** | “The agent may prepare drafts and run checks. Every client-facing assessment needs human review. Known boundary failures block release, and the bank reviewer owns risk acceptance.” |

## If you have 20 extra seconds

Open the [successful GitHub Actions run](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33901467965). Point to the completed calibration and evaluation steps.

Say: “GitHub records the code and automated workflow. Weave records the application calls and evaluation evidence. Green workflow checks mean execution completed; they do not mean every case passed.”

## Labels you may see

| Label | Simple explanation |
| --- | --- |
| Call | One recorded software step |
| Trace | The connected record of a run |
| Dataset | Repeatable test cases |
| Evaluation | Run cases and grade the outputs |
| `score_references` | Are the source, passage, and quotation valid? |
| `score_status` | Do the evidence status and conditional scope follow exact rules? |
| `BankRiskJudge` | AI review of evidence support, scope, and follow-up quality |
| `gate_record` | What V2 rejected and why |
| Pass | Automated rules accepted the assessment—not the vendor |
| Block | Policy prevents report release |
| Unknown | Insufficient evidence to grade; never a pass |
| `git_commit` | Code revision used for the run |
| `sha256` | File fingerprint, not a risk score |

## Limitations to say clearly

- “C02 still has a readiness-state mismatch the graders missed.”
- “The C05 judge interpretation is unreliable and needs human adjudication.”
- “There is one fictional vendor and five assessment cases.”
- “The 22 regression tests and 23 offline stress probes are not additional live model cases.”
- “Public SOC documents were provenance-tested; they were not used for a completed model risk assessment.”
- “The proposed 30-day rule has not started a real bank pilot.”

## Closing line

> “V2 caught the targeted unknown-scope error, but readiness-state and judge limitations remain. I would keep this assistant in draft-only use with human review and improve the evaluation before expanding automation.”

## If a page does not load

- GitHub: return to the [repository home](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents), confirm the branch is `main`, and select the file.
- Weave login/404: sign in to the W&B account with access to `kevinmedeiros-masterclass/ai-lab-agent-governance`, then reopen the link. Do not change sharing permissions or show an API key.
- Cannot find C03: use browser Find for `C03`, or return to CURRENT_COMPARISON.md and follow the C03 instructions.

For a longer rehearsal explanation, use [GITHUB_RECORDING_GUIDE.md](GITHUB_RECORDING_GUIDE.md). For the submission checklist, use [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md).
