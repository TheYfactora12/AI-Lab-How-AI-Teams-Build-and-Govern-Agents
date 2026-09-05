# GitHub recording guide

This is the click-by-click route for presenting the completed certificate experiment. Keep this page open as your private guide. The current evidence is contract 1.4; files labeled historical explain earlier work and should not be used for current result counts.

## Before you record

1. Sign in to GitHub and W&B in the browser you will record.
2. Open the [repository home](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents).
3. Open every link in the **Recording tabs** table below in a separate tab, in that order.
4. Increase browser zoom until the text is readable in your recording.
5. Close or hide tabs containing email, account settings, API keys, notifications, or unrelated personal information.
6. Test the two private Weave links. A login/404 page usually means the recording browser is not signed into the W&B account with project access; do not make the project public to fix navigation.

## How GitHub is organized

On the repository’s **Code** page, the top list contains folders and files. A file ending in `.md` is a readable project page. Select its name to open it. Use the repository breadcrumb or browser Back button to return to the file list.

| GitHub item | Plain-English meaning | Use in recording? |
| --- | --- | --- |
| README.md | Front door and project status | Yes—start here |
| START_DEMO_HERE.md | Short preparation checklist | Use before recording |
| CURRENT_COMPARISON.md | Authoritative current results and direct evidence | Yes—main results page |
| USE_CASE_PROFILE.md | Fictional bank, vendor, users and boundaries | Yes—business problem |
| EVALUATION_DESIGN.md | Test cases and definitions of good behavior | Yes—show briefly |
| OPERATING_POLICY.md | Automate/review/block decision | Yes—finish here |
| VIDEO_WALKTHROUGH.md | Suggested narration | Use as rehearsal notes |
| bank_review/ | Python implementation | Show only gate.py if desired |
| data/ | Synthetic cases, catalog and expected results | Show the case table in the design instead of raw JSON unless asked |
| evaluation_snapshots/contract-1.4/ | Exact saved outputs and receipt | Backup evidence; JSON is hard to present live |
| COMPARISON_REPORT.md | Historical contract 1.1 comparison | Do not use for current counts |
| PROJECT_EVIDENCE_WALKTHROUGH.md | Historical first-loop walkthrough | Do not use as the main current walkthrough |
| STRESS_TEST_REPORT.md | Original stress failures | Mention only to explain why the correction was made |

## Recording tabs

| Order | Open this | What it proves |
| ---: | --- | --- |
| 1 | [Repository README](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/README.md) | This is an Evaluation Builder project and identifies the current evidence |
| 2 | [Use-case profile](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/USE_CASE_PROFILE.md) | The application, intended user, data boundaries and prohibited authority |
| 3 | [Evaluation design](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/EVALUATION_DESIGN.md) | Five cases, exact checks, judge rubric and controlled comparison design |
| 4 | [Current comparison](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/CURRENT_COMPARISON.md) | Actual contract 1.4 results, limitations and direct W&B links |
| 5 | [Current V1 in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fc-9244-721f-894e-d4bb3ecf9ec1) | C03’s V1 scope error and exact failure |
| 6 | [Current V2 in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fd-071e-7eeb-8a8f-fe0cf744302a) | C03’s rejected scope decisions and withheld assessment |
| 7 | [V2 gate code](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/bank_review/gate.py) | The single V2 post-generation intervention |
| 8 | [Successful workflow](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33972108376) | Tests and both hosted evaluations executed successfully |
| 9 | [Operating policy](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/OPERATING_POLICY.md) | Current automate/review/block decision and owners |

The Weave links are private project links. They can work for you while returning 404 to someone without access. The committed [receipt](evaluation_snapshots/contract-1.4/receipt.json) preserves their identifiers and the executed source revision.

## Four-minute click route

### 1. README — 15 seconds

Point to the title and the **Current project status** box.

Say: “I selected the Evaluation Builder track and built a banking vendor-risk review assistant in Python with W&B Weave.”

Do not read the whole repository listing. The folders are implementation evidence, not the story.

### 2. Use-case profile — 30 seconds

Point to **The two systems**, **Business problem**, and **Permitted output and decision authority**.

Say: “The fictional vendor provides an internal policy assistant. My application reviews its intended use and evidence for a banking consultant. It drafts an assessment; it cannot approve the vendor or authorize a deployment.”

### 3. Evaluation design — 35 seconds

Scroll to **Five-case dataset**. Show C01 through C05. Briefly show **Deterministic scorers** and **Live judge**.

Say: “The dataset covers normal evidence, a missing test, unknown scope, a retrieval timeout and contradictory sources. Exact rules check citations and evidence status. A three-criterion AI judge evaluates support, scope and follow-up quality.”

Do not call the 23 regression tests or 31 offline probes additional model cases. There are five live cases per version.

### 4. Current comparison — 40 seconds

Point to **What matters** and the C03 row.

Say: “V1 received three passes and two blocks. V2 received three passes, one block and one review because C05 failed schema validation and was withheld. Case-level inspection matters.”

Explain that these are assessment-quality results, not vendor approvals or production failure rates.

### 5. V1 C03 in Weave — 40 seconds

Use the direct V1 link. Locate C03 by its case input. Expand the relevant prediction and `score_status` call.

Show that `restricted_documents` and `credit_decisions` are null. Show the exact reason: SEC-01 and FAIR-02 scope contradict the intended-use fields.

Say: “Null means the bank has not answered the question. V1 converted unknown information into scope conclusions, and the corrected exact scorer blocks that.”

If W&B generated names are visible, explain that names such as rich-oak are automatic labels. Locate the case by C03, not by the generated label.

### 6. V2 C03 in Weave — 45 seconds

Use the direct V2 link. Locate C03 and expand `apply_evidence_gate`. Open `gate_record` in the output.

Show the three rejected findings, `needs_clarification`, `packet_status: withheld`, and the clarification questions.

Say: “V2 adds a validation gate after generation. It catches two unsupported scope decisions plus one requirement-mismatched citation, preserves uncertainty and sends the issue to a person.”

Green execution status means the software call completed. It does not mean the vendor or assessment passed. Explain `score_references`, `score_status`, and `BankRiskJudge` using the plain-English table in CURRENT_COMPARISON.md.

### 7. Gate code and workflow — 25 seconds

On `bank_review/gate.py`, point to `@weave.op` and `apply_evidence_gate`. There is no need to explain every line.

Say: “The Weave operation records the gate’s input and output. GitHub preserves the implementation, and this Actions run shows the tests and controlled evaluations completed.”

On the Actions page, green checks mean workflow steps completed. They do not mean every evaluation case passed.

### 8. Operating policy — 30 seconds

Point to **Routing rules** and **Team ownership**.

Say: “The assistant may prepare drafts and checks. Every client-facing assessment needs human review. Known boundary failures block report release, and the bank reviewer owns risk acceptance.”

Close with: “V2 caught the targeted scope and citation-boundary errors, but readiness and generation reliability remain limited. I would keep the system in draft-only use while adding repeated trials and a direct readiness check.”

## What each result means

| Screen label | Say this |
| --- | --- |
| Green execution icon | “The function completed without a system error.” |
| Pass | “The automated evaluation accepted this assessment under the current rules.” |
| Block | “The current policy prevents report release.” |
| Unknown | “The grader lacks evidence to decide; it does not count as a pass.” |
| `score_references` | “Are the source identity, passage and quotation valid?” |
| `score_status` | “Do evidence status and conditional scope follow the exact rules?” |
| `BankRiskJudge` | “An AI model reviews support, scope and follow-up quality; its interpretation can be wrong.” |
| `gate_record` | “This records what V2 rejected and why.” |
| `git_commit` | “This identifies the code revision used for the run.” |
| `sha256` | “This fingerprint detects changed files; it is not a risk score.” |

## Statements to avoid

- “V2 is completely fixed.”
- “The vendor passed.”
- “Three out of five vendors were approved.” There is one fictional vendor and five assessment cases.
- “The stress tests prove production readiness.”
- “We evaluated the public SOC reports with the model.” Public-document intake only verified provenance.
- “The judge is ground truth.” C02 shows a remaining readiness-scoring problem; V2 C05 shows generation variability.
- “The 30-day pilot already started.” It is a proposed operating rule.

## If navigation goes wrong

- **GitHub file not found:** return to the repository home, confirm the branch selector says `main`, then select the file from the Code list.
- **Weave login/404:** sign in to W&B using the account with access to `kevinmedeiros-masterclass/ai-lab-agent-governance`, then reopen the direct link. Do not expose the API key on screen.
- **Cannot locate C03:** use browser find for `C03`. If the Weave layout differs, find the row/call whose input contains the C03 case. Use CURRENT_COMPARISON.md as the map.
- **JSON is hard to read:** return to CURRENT_COMPARISON.md. Raw snapshots are audit evidence and do not need to be presented unless asked.
- **Judge wording seems inconsistent:** say that the raw output is preserved and human adjudication is part of the documented operating policy.

## Final readiness check

The repository includes a repeatable [presentation link audit](presentation_snapshots/link-check.json). It verifies local targets, maps GitHub file links to tracked paths, and matches the private Weave URLs and Actions run to the successful contract 1.4 receipt. It cannot prove that a different browser is signed in to the private W&B project.

- [ ] All nine recording tabs open while signed in.
- [ ] You can locate C03 in both Weave evaluations.
- [ ] You can explain `null` as unknown, not no.
- [ ] You can show V1's exact failure and V2's gate rejection.
- [ ] You can explain why aggregate verdict counts alone do not establish improvement; the C03 gate record is the direct evidence.
- [ ] You can name the C02 readiness and V2 C05 generation limitations.
- [ ] No credential, account-setting page or unrelated personal tab is visible.
- [ ] Your narration is in your own words and lasts 3–5 minutes.

Use [VIDEO_WALKTHROUGH.md](VIDEO_WALKTHROUGH.md) for rehearsal and [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) before uploading.
