# Current recording outline: contract 1.4

Use your own voice and judgment. This four-minute outline covers the corrected implementation. For condensed talking points, open the [recording cheat sheet](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/RECORDING_CHEAT_SHEET.md). The first experiment and its older C02 intervention are historical evidence.

## Open these links before recording

1. [Repository README](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/README.md)
2. [Use-case profile](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/USE_CASE_PROFILE.md)
3. [Evaluation design](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/EVALUATION_DESIGN.md)
4. [Current comparison](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/CURRENT_COMPARISON.md)
5. [Current V1 evaluation in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fc-9244-721f-894e-d4bb3ecf9ec1)
6. [Current V2 evaluation in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fd-071e-7eeb-8a8f-fe0cf744302a)
7. [Operating policy](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/OPERATING_POLICY.md)

## 0:00–0:40: Problem

Screen: [README project status](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/README.md), then [use-case profile](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/USE_CASE_PROFILE.md).

“My project helps a banking consultant review an AI vendor's evidence for a specific intended use. I chose an internal policy assistant and fictional documents. The assistant drafts findings and questions; a person owns the final assessment. I selected the Evaluation Builder track and implemented the application in Python with Weave tracing.”

## 0:40–1:20: Define and evaluate good behavior

Screen: [five-case dataset in Weave](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/objects/bank-vendor-scope-five-v1/versions/Ew78A6FsNIIFMK8IlXgz8J6HdAX9iaeMqlUltbJRPQs), [evaluation design](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/EVALUATION_DESIGN.md), and [judge rubric](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/JUDGE_RUBRIC.md).

“Good behavior means selecting relevant requirements, citing the right evidence, and preserving uncertainty. We use five cases: normal evidence, a missing test, unclear scope, a retrieval timeout and conflicting statements. Two exact scorers check evidence and status rules, and an AI judge reviews evidence support, scope and follow-up quality. The same test contract applies to both versions.”

## 1:20–2:20: Show the actual corrected V2 change

Screen: [current V1 C03 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fc-9244-721f-894e-d4bb3ecf9ec1), then [current V2 C03 evaluation](https://wandb.ai/kevinmedeiros-masterclass/ai-lab-agent-governance/weave/calls/01a071fd-071e-7eeb-8a8f-fe0cf744302a). Use the [current comparison](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/CURRENT_COMPARISON.md) to identify what to find.

“In C03, the bank's restricted-document access and credit-decision role are unknown. V1 makes unsupported scope decisions. Our corrected exact check catches that. V2 adds a post-generation validation gate: it marks those requirements as needing clarification and withholds the draft. Here are the input, the rejected scope decisions and the resulting questions.

“The gate also rejects malformed records, duplicate identifiers and eight documentary citation-boundary mutations found during independent stress testing. Shared validation, scoring and judge corrections apply to both versions. I keep this rerun separate from the original experiment.”

## 2:20–3:20: Results and limitations

Screen: [current comparison and result table](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/CURRENT_COMPARISON.md). Optional evidence: [successful GitHub Actions run](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/actions/runs/33972108376) and [corrected stress review](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/V2_CORRECTION_RECORD.md).

“V1 received three passes and two blocks. V2 received three passes, one block and one review. In C03, V2 contained the targeted scope error and a requirement-mismatched citation.

“Inspection still matters. In C02, both versions mark the packet ready even though the expected result calls for more evidence. The judge misses that. In C05, V1 produced an unresolved assessment but the judge reasoning was unreliable, while V2 produced schema-invalid output. V2 safely withheld it and skipped the judge. This proves fail-closed routing, while also showing that model generation is not perfectly repeatable.

“The corrected code passed 23 assessment tests and six intake tests. The 31 offline stress probes met their expectations. Those probes are separate from the five live model cases.”

## 3:20–4:00: Operating decision

Screen: [operating policy](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/OPERATING_POLICY.md) and [V2 correction record](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/V2_CORRECTION_RECORD.md).

“My deliverable connects code, test cases, traces, grading rules and a documented operating decision. The assistant stays in draft-only use with human review. The consultant interprets evidence, the bank reviewer owns risk acceptance, and the technical owner can stop the workflow. Before expanding, I would improve readiness checks, calibrate the judge and obtain expert review of more cases.”

Review these statements yourself before recording. Use the [GitHub navigation guide](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/GITHUB_RECORDING_GUIDE.md) if a screen is unfamiliar, and finish with the [submission checklist](https://github.com/TheYfactora12/AI-Lab-How-AI-Teams-Build-and-Govern-Agents/blob/main/SUBMISSION_CHECKLIST.md). Open each trace while signed in, hide credentials, check sound and readability, and submit a 3–5 minute recording in your own voice. No video or course submission has been completed by the coding agent.
