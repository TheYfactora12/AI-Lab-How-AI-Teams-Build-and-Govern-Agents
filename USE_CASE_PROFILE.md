# Use-case profile: Internal bank policy assistant

Profile ID: UC-001
Version: 1.0
Status: Working design for the certificate project
Source: Synthetic scenario; all organizations, systems, and operating rules below are fictional design choices, not legal requirements or verified vendor capabilities.

## The two systems

The vendor product under review is **PolicyDesk**, supplied by fictional **CedarBridge AI**, vendor ID `VENDOR-001`.

The client is fictional **Harbor Glen Community Bank**, bank ID `BANK-001`.

Our application is the **Vendor Risk Assessment Assistant**. It reviews PolicyDesk's intended use and evidence. Weave evaluations test our assessment assistant's work. A simulated evidence packet does not establish that a real PolicyDesk implementation exists or passes security tests.

## Business problem

Bank employees spend time locating the current version of internal policies and deciding who can answer exceptions. The proposed vendor assistant would help them find relevant passages and draft concise, cited answers. The consulting engagement determines what must be assessed and what evidence is still needed before the bank considers a limited pilot.

The potential benefits are less search time and fewer answers based on obsolete policy. These are hypotheses; this certificate project does not measure actual employee productivity.

## Intended users and questions

A proposed pilot includes 20 designated branch-operations and IT-support employees. A policy owner and security reviewer oversee it. No customers or external parties use the assistant.

Example questions:
- Where is the current procedure for requesting temporary access?
- Which team receives a suspected phishing report?
- Where can I find the approved branch-opening checklist?

If a question needs a personal exception or a decision affecting a customer, the assistant provides the authorized escalation route and does not decide the outcome.

## Data and access boundaries

| Data or capability | Proposed boundary | Assessment implication |
| --- | --- | --- |
| Approved internal policy library | Read-only access to current, approved documents | Verify approval/version metadata and handling of stale sources |
| Role-restricted policy pages | Retrieve only passages the signed-in user is allowed to read | Require entitlement design evidence and role-isolation tests |
| Employee identity | Pseudonymous user ID and authorized role claims supplied by bank sign-in | Review identity mapping, access revocation, and log minimization |
| Employee questions | Work-related questions; users may accidentally enter sensitive text | Assess handling of prohibited input, retention, and support access |
| Customer/account records | No connector or authorized access | Verify connector scope; do not assume sensitive data can never enter via a prompt |
| Employee personnel/payroll records | No connector or authorized access | Verify scope and routing for questions seeking personal information |
| Internet and external tools | No open web browsing, email sending, or external action tools | Review actual tool inventory and outbound data paths |
| Bank systems | No writes, transactions, account changes, or access grants | Require permission evidence; text instructions are insufficient proof |

Data sent to any model provider, logging service, or subprocessor must be documented. Hosting region, retention periods, deletion behavior, support access, and model-training terms are unknown until supplied evidence establishes them. Unknown values must remain visible.

## Permitted output and decision authority

PolicyDesk may draft an answer using authorized policy passages, cite document ID/version and passage, identify uncertainty, and give a policy-approved escalation route.

It may not approve transactions, determine credit eligibility, make employment decisions, grant exceptions, change records, or represent its answer as a binding bank decision. Staff remain responsible for following approved procedures and escalating uncertainty.

If evidence is missing, conflicting, inaccessible, expired under bank rules, or unavailable because retrieval failed, it must acknowledge the limitation and route the question to the appropriate human owner. It must not expose restricted passages while explaining why access was denied.

## Risk areas and why they apply

| Area | Applicability for this scenario | Evidence to request |
| --- | --- | --- |
| Use and impact | Incorrect policy answers can misdirect staff even without transaction authority | Intended-use statement, affected workflows, prohibited uses, accountability map |
| Data and privacy | Internal content and user questions may reach vendor systems | Data-flow diagram, training terms, retention/deletion rules, subprocessor list |
| Security | Role-restricted retrieval and document/prompt injection create exposure risks | Identity/permission design, tool inventory, tenant/role isolation tests, injection tests, incident process |
| Model quality | Answers need current, relevant sources and accurate citations | Evaluation design/results for factual support, citations, stale sources, ambiguity, and abstention |
| Fairness and accessibility | Employees may use different phrasing or need accessible output | Tests across relevant wording and accessibility needs; documented limitations |
| Human oversight | Staff need a clear way to escalate and report incorrect answers | Escalation procedure, accountable owners, stop mechanism, feedback workflow |
| Vendor governance and resilience | Model updates or outages can invalidate prior review or remove access to guidance | Change notices, version records, continuity plans, export/deletion and exit procedures |

Credit-outcome discrimination testing is not applicable to the stated use because the assistant does not participate in lending decisions. That exclusion must be reassessed if scope changes; it is not a blanket claim that fairness is irrelevant. The catalog will distinguish these use-specific requirements rather than treating each broad area as a universal pass/fail item.

## Evidence discipline for our assessment assistant

Every finding should record the requirement ID, applicability rationale, vendor ID, source ID/version, supporting passage or test reference, evidence type, unresolved gap, and suggested owner.

Keep three evidence types separate:
1. **Vendor assertion:** The vendor says a control exists.
2. **Documented support:** A policy or design document describes the control; record whether it is vendor-authored.
3. **Observed test result:** A supplied test record reports behavior under specified conditions, with system version, date, method, and limits. Synthetic records remain explicitly labeled synthetic.

A stronger evidence type does not guarantee overall safety. One passing test supports only the behavior and conditions it tested. Conflicting evidence must be reported, not averaged into a favorable score.

Examples of expected assessment behavior:
- A policy says role isolation exists but no test record is supplied: request testing and mark behavior unverified.
- A questionnaire says prompts are never used for training while contract terms allow it: cite the contradiction and request resolution.
- The intended tool access is unspecified: ask about access before finalizing the assessment scope.

## Human ownership and reversible pilot proposal

These are role assignments for the simulation, not actual personnel assignments or an approved deployment.

- Consultant: checks the assessment scope, evidence interpretation, and client-facing packet.
- Bank policy owner: resolves policy ambiguity and maintains approved sources.
- Bank security/vendor-risk reviewer: accepts or rejects residual risks and the pilot proposal.
- Bank IT owner: controls integrations, access, logging, and shutdown.
- Vendor contact: supplies evidence and explains changes and limitations.

A proposed 30-day pilot would use the stated users and read-only scope, with ordinary policy search as fallback. A restricted-data disclosure or unsupported consequential instruction triggers suspension and human investigation. Missing approval evidence prevents pilot clearance. Any expansion requires a new assessment.

The certificate deliverable is a draft assessment packet, not authorization to run this pilot. Human review is required before any client-facing assessment is released.

## Scope-change triggers

Reassess if the assistant gains customer-facing use, customer or personnel data access, write/action tools, involvement in credit or employment decisions, new subprocessors, changed training/retention terms, a material model/retrieval update, or evidence of a significant failure.

## Completion boundary and next step

This file defines the scenario. It does not supply vendor evidence, finalized scoring rules, measured performance, or compliance conclusions.

Next: Convert these requirements into a versioned assessment catalog and five synthetic evidence packets with independently specified expected findings. Freeze the evaluation contract before comparing V1 and V2.

Project requirements: https://github.com/LorenzoWandB/PatchPilot-MasterClass/tree/main/certificate-project
