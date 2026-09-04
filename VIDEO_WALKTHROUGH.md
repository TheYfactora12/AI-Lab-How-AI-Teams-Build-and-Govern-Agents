# Recording outline: 3–5 minutes in your own voice

Personalize this preparation script before recording. Explain your own choices and disagreements. Show the actual files and Weave results; do not read credentials or use an AI voice. Aim for about four minutes, allowing time to open the traces.

## 0:00–0:40 — Problem and intended user

Screen: PROJECT_BRIEF.md and USE_CASE_PROFILE.md.

“My project is an AI-assisted scope and evidence review for a banking security consultant. The question is whether a vendor's evidence supports the bank's intended use, and what still needs investigation. A fixed checklist can miss the context: an internal policy assistant has different risks from a system making credit decisions.

“I chose a fictional community bank and vendor so I could demonstrate the workflow without using customer information. The assistant prepares a review packet. A person remains responsible for the assessment and any client report.”

## 0:40–1:25 — Define good behavior and evidence

Screen: EVALUATION_DESIGN.md, then one case in data/cases.jsonl.

“Good behavior means selecting relevant requirements, citing actual supplied passages, separating vendor assertions from observed tests, and asking specific questions when evidence is missing. Unknown information must stay unknown.

“I designed five synthetic cases: normal evidence, a missing role-isolation test, ambiguous scope, a retrieval timeout and contradictory documents. Two exact scorers check reference integrity and evidence status. A live AI judge grades evidence support, scope and follow-up quality. A known exact failure blocks release even when the judge passes it.”

## 1:25–2:15 — Show the controlled change

Screen: V1 C02 evaluation, then V2 C02 gate and final output.

“Both versions use the same model, prompt, dataset and scoring contract. V2 adds one evidence-validation gate after generation.

“Here is the useful failure: V1 cited a real injection test as support for role isolation. The citation existed, but it tested the wrong requirement. The exact status scorer caught that mismatch; the AI judge missed it.

“V2's gate caught the mismatch and withheld the draft. Its exact status result changed from fail to pass. Withholding the whole draft also removes useful findings, so this is containment with a tradeoff, not a complete solution.”

## 2:15–3:15 — Results and evaluation weaknesses

Screen: COMPARISON_REPORT.md result table and C03/C05 observations.

“Overall, both versions received three automated passes and two blocks. I cannot claim an overall score improvement.

“More importantly, inspecting the output showed that C03 treated an unknown credit-decision field as no credit decisions. Every scorer passed it. That means the evaluation itself needs better coverage. In the normal case, the judge also missed a mismatch with the expected review state.

“Both versions failed to produce valid structured assessments for the contradiction case. Those errors were recorded explicitly. The judge then described a claim that was not in the empty output. I preserved the original scores and documented the disagreement instead of making the results look better.

“The lesson is that a passing dashboard is evidence to inspect, not permission to trust the report.”

## 3:15–4:05 — Final deliverable and operating decision

Screen: OPERATING_POLICY.md, then repository README.

“The deliverable is this reproducible evaluation package: five cases, two versions, exact checks, a judge rubric, Weave traces, a comparison report and a proposed 30-day operating rule.

“The assistant stays limited to synthetic draft preparation. Every report needs human review. The consultant owns evidence interpretation, the bank reviewer owns risk acceptance, and the technical owner can disable the workflow and return to manual review.

“Before expanding, I would improve scope checking and judge calibration, obtain expert review of the answer key, and test more cases repeatedly. The project demonstrates how I would govern an assessment assistant, while making its current limitations visible.”

Before upload: add your own motivation and judgment, verify all shown results, check duration and sound, and submit the recording through the course interface. No video has been created or submitted by the agent.
