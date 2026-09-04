# Reversible 30-day operating rule

Policy version: draft-assessment-v1.0. This is a proposed simulation policy, not an approved bank deployment. Its 30-day period begins only when a designated owner approves a controlled pilot; no pilot is started by this document.

## Operating scope

The assessor may automatically prepare drafts from the fixed synthetic vendor packets, record Weave traces and apply exact checks. It cannot approve vendors, authorize a bank pilot, change bank systems or send reports to customers. Every client-facing assessment requires consultant and bank-owner review.

## Routing rules

| Condition | Required action | Owner |
| --- | --- | --- |
| All exact checks and judge criteria pass | Queue the draft for human review; do not auto-release | Consultant |
| Missing evidence, unclear applicability, incomplete judge or infrastructure failure | Mark unresolved items; request evidence or retry only after diagnosing the failure | Consultant and evidence owner |
| Any deterministic failure or blocking judge failure | Block report release; inspect original draft and cited evidence | Bank security/vendor-risk reviewer |
| V2 gate withholds a draft | Keep the original only in the trace; produce an evidence request for human action | Consultant |
| Human reviewer disputes a judge result | Record the reason and source references; preserve the original model verdict | Consultant, adjudicated by bank reviewer |

The vendor packet's needs_evidence status and the assessor's evaluation verdict are different decisions. A correct request for missing evidence may pass the evaluation. A real source citation may still support an overbroad claim and require a block.

## Team ownership

- Consultant: applicability decisions, evidence interpretation, final narrative and client delivery.
- Bank security/vendor-risk reviewer: residual-risk decisions and approval of any future pilot.
- Policy owner: source currency and resolution of policy conflicts.
- Bank IT owner: access/integrations, tracing configuration and disabling the workflow.
- Vendor contact: source records, test methods/results and change notices.
- Accessibility/model-risk specialists: relevant user impact and consequential-decision reviews when scope requires them.

These are fictional role assignments; named people and sign-off records must be supplied before real use.

## Stop and rollback

Stop automated report preparation if restricted information crosses a vendor/user boundary, a report invents material evidence, trace records needed for review are unavailable, or an unsupported consequential recommendation reaches a reviewer unflagged. Preserve the failed trace and suspend the workflow; bank IT can disable the manual workflow/integration. Fall back to manual document review using the same catalog. Re-enable only after a documented cause, fix and regression check.

## Review cadence and expansion evidence

During an approved pilot, the consultant reviews every draft and keeps corrections by requirement and case. Weekly reviews inspect missed material gaps, unsupported claims, irrelevant escalations, source versioning and judge disagreement. Day 30 is a decision point: retain the bounded scope, revise and retest, or end the pilot.

Before expansion, require expert-reviewed cases beyond these five, more vendors and employee roles, adversarial/permission cases, repeated trials, independent judge calibration, measured correction burden, and an explicit privacy/access review. Testing a vendor's actual system requires separate authorization and observed evidence; supplied fictional test records do not substitute for that work.

## Confidence and evidence limit

The local implementation checks and live comparison support review of this bounded prototype. They do not establish production readiness. Confidence in unattended client-facing decisions remains low. Actual case outcomes and reasons are recorded in [COMPARISON_REPORT.md](COMPARISON_REPORT.md); the above fixed release-routing rule applies equally to V1 and V2.
