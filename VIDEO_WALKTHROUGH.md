# Current recording outline: contract 1.2

Use your own voice and judgment. This four-minute outline covers the corrected implementation. Keep the [current comparison](CURRENT_COMPARISON.md) open for exact results. The first experiment and its older C02 intervention are historical evidence.

## 0:00–0:40: Problem

Screen: USE_CASE_PROFILE.md.

“My project helps a banking consultant review an AI vendor's evidence for a specific intended use. I chose an internal policy assistant and fictional documents. The assistant drafts findings and questions; a person owns the final assessment. I selected the Evaluation Builder track and implemented the application in Python with Weave tracing.”

## 0:40–1:20: Define and evaluate good behavior

Screen: five-case dataset, EVALUATION_DESIGN.md and JUDGE_RUBRIC.md.

“Good behavior means selecting relevant requirements, citing the right evidence, and preserving uncertainty. We use five cases: normal evidence, a missing test, unclear scope, a retrieval timeout and conflicting statements. Two exact scorers check evidence and status rules, and an AI judge reviews evidence support, scope and follow-up quality. The same test contract applies to both versions.”

## 1:20–2:20: Show the actual corrected V2 change

Screen: current V1 and V2 C03 traces, linked in CURRENT_COMPARISON.md.

“In C03, the bank's restricted-document access and credit-decision role are unknown. V1 makes unsupported scope decisions. Our corrected exact check catches that. V2 adds a post-generation validation gate: it marks those requirements as needing clarification and withholds the draft. Here are the input, the rejected scope decisions and the resulting questions.

“The gate also rejects the malformed records and duplicate identifiers found in our offline stress tests. Shared validation, scoring and judge corrections apply to both versions. I keep this rerun separate from the original experiment.”

## 2:20–3:20: Results and limitations

Screen: CURRENT_COMPARISON.md.

“Both versions received three automated passes and two blocks. Both produced valid assessments for all five cases in this run. The gate contained the targeted scope error, but there is no overall pass-count gain.

“Inspection still matters. In C02, both versions mark the packet ready even though the expected result calls for more evidence. The judge misses that. In C05, the agent shows contradictory sources, but the judge misinterprets the conflict. We preserve those scores and explain the disagreement; we do not claim the system is fully accurate.

“The corrected code passed 22 assessment tests and six intake tests. The 23 offline stress probes met their expectations. Those probes are separate from the five live model cases.”

## 3:20–4:00: Operating decision

Screen: OPERATING_POLICY.md and V2_CORRECTION_RECORD.md.

“My deliverable connects code, test cases, traces, grading rules and a documented operating decision. The assistant stays in draft-only use with human review. The consultant interprets evidence, the bank reviewer owns risk acceptance, and the technical owner can stop the workflow. Before expanding, I would improve readiness checks, calibrate the judge and obtain expert review of more cases.”

Review these statements yourself before recording. Open each trace while signed in, hide credentials, check sound and readability, and submit a 3–5 minute recording in your own voice. No video or course submission has been completed by the coding agent.
