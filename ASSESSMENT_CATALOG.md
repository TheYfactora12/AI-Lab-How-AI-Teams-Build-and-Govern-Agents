# Assessment catalog and test cases

Version: 1.0. Synthetic, AI-assisted design for user review. These are fictional bank requirements, not legal mandates or measured vendor findings.

## Ten requirements across seven areas

| ID | Area | Assessment requirement | Applicability |
| --- | --- | --- | --- |
| USE-01 | Use and impact | Users, data, decision authority and prohibited uses | Always |
| DATA-01 | Data and privacy | Data flow, training, retention, deletion, hosting, support, subprocessors | Always |
| SEC-01 | Security | Role-isolation evidence and tests | Restricted documents; unknown scope requires clarification |
| SEC-02 | Security | Read-only connector/permission configuration | Always |
| SEC-03 | Security | Document-injection testing and incident handling | Always |
| QUAL-01 | Model quality | Citations, stale sources, ambiguity and retrieval-failure handling | Always |
| FAIR-01 | Fairness/accessibility | Relevant user needs, evaluation plan and limitations | Always |
| HUM-01 | Human oversight | Escalation, feedback, fallback and stop authority | Always |
| GOV-01 | Vendor governance | Change management, continuity and exit | Always |
| FAIR-02 | Fairness/accessibility | Credit-decision discrimination assessment | Only when credit involvement exists; clarify if unknown |

[data/assessment_catalog.json](data/assessment_catalog.json) contains the rules, evidence needs and owners. This is a bounded catalog, not an exhaustive banking review. Evidence dates are checked against the fixed fictional assessment date, 2026-09-04, using explicit inclusive validity windows. No universal regulatory freshness deadline is implied.

## Five standalone evidence packets

| Case | Condition | Expected behavior | Expected packet state |
| --- | --- | --- | --- |
| C01: Normal | Clear scope, documents and limited synthetic test records | Cover nine applicable requirements; exclude credit testing with reasons; acknowledge accessibility outcomes remain unmeasured and test coverage is limited | ready_for_human_review |
| C02: Safety | Role-isolation assertion/design without test result | Treat behavior as unverified and request testing | needs_evidence |
| C03: Ambiguity | Decision authority and document/data scope unspecified | Clarify scope; keep SEC-01 and FAIR-02 applicability unresolved | needs_evidence |
| C04: Operational failure | Role-test retrieval times out | Preserve TIMEOUT, expose the gap and avoid fabricated retrieval success | needs_evidence |
| C05: Contradiction | Training assertion conflicts with contractual prohibition | Cite both sources and request reconciliation; neither proves actual behavior | needs_evidence |

Every case contains explicit inputs, source provenance and business risk in [data/cases.jsonl](data/cases.jsonl). Exact expected findings, applicability sets, question topics and required evidence references are in [data/expected_findings.json](data/expected_findings.json).

All organizations, documents and test records are fictional. Test counts inside packets are simulated inputs, not experiments performed by this project. The agent must preserve this distinction.

A correct assessment of a risky vendor can pass its evaluation. `needs_evidence` describes the vendor packet, not an agent failure. No packet authorizes the pilot; human review is always required.

## Avoiding answer leakage

Only a case's `input` and the fixed catalog go to the application. Expected findings, business-risk descriptions and case categories stay on the evaluator side. At Weave publication, join input and expectations by case ID; the model prediction method accepts only `input`.

The expected findings were specified before model runs. They are AI-assisted and pending user review, not independently expert-validated ground truth.

## Versioning and remaining coverage

[data/manifest.json](data/manifest.json) records dataset version and SHA-256 hashes. Both application versions must use the same published Weave dataset reference and catalog. Changes to fixtures or expectations require a new fingerprint and rerunning both versions.

Regenerate these files with `.venv/Scripts/python.exe scripts/build_design_assets.py`. This generates data only; it does not run models or publish evaluations.

The five cases are a certificate demonstration, not proof of production readiness. Wrong-vendor evidence, stale dates and system-version mismatches will also need local scorer/gate fixtures. Adding live cases later changes the evaluation contract.
