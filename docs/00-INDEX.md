# RUKSA Document Index

**Edition:** 1.1 (Fabric vision addendum) · **Baseline date:** 2026-11-02 · **Owner:** YanIanZ · **Status:** planned, not implemented.

RUKSA is a product specification for an evidence-first autonomous procurement agent under the Vultr **Blast Radius Zero** challenge. All prescriptive choices are proposed implementation designs, not statements about deployed functionality.

| Doc | Purpose | Review owner |
|---|---|---|
| [01-PRD](01-PRD.md) | Product scope, jobs, personas, acceptance | PM |
| [02-ARCHITECTURE](02-ARCHITECTURE.md) | Boundaries, topology, data flow | Tech lead |
| [03-TECHNICAL-SPEC](03-TECHNICAL-SPEC.md) | Runtime contracts and nonfunctional requirements | Engineering |
| [04-API-CONTRACT](04-API-CONTRACT.md) | REST/SSE interface | Backend |
| [05-DATA-MODEL](05-DATA-MODEL.md) | Tables, indexes, lifecycle | Backend |
| [06-SECURITY-THREAT-MODEL](06-SECURITY-THREAT-MODEL.md) | Threats and mitigations | Security |
| [07-AGENT-ORCHESTRATION](07-AGENT-ORCHESTRATION.md) | Agent prompts, tools, limits and states | AI engineering |
| [08-EVIDENCE-PROTOCOL](08-EVIDENCE-PROTOCOL.md) | Evidence binding, verification, provenance | AI/Backend |
| [09-UX-UI](09-UX-UI.md) | Interaction patterns and accessibility | Frontend |
| [10-IMPLEMENTATION-ROADMAP](10-IMPLEMENTATION-ROADMAP.md) | D1–D6 milestones, critical path | PM |
| [11-BACKLOG](11-BACKLOG.md) | Work packages and acceptance criteria | Engineering |
| [12-TEST-PLAN](12-TEST-PLAN.md) | Unit/integration/safety/E2E test plan | QA |
| [13-DEPLOYMENT-OPERATIONS](13-DEPLOYMENT-OPERATIONS.md) | Vultr runbook, budget and observability | DevOps |
| [14-DEMO-AND-SUBMISSION](14-DEMO-AND-SUBMISSION.md) | Video, submission assets, rubric mapping | PM |
| [15-BUSINESS-AND-METRICS](15-BUSINESS-AND-METRICS.md) | Economics, value and KPI caveats | Product |
| [16-DECISION-RECORDS](16-DECISION-RECORDS.md) | Architectural decisions and trade-offs | Tech lead |
| [17-DATASET-SPEC](17-DATASET-SPEC.md) | Synthetic benchmark ground truth | Data/QA |
| [18-RISK-REGISTER](18-RISK-REGISTER.md) | Scope, cost, operational risks | PM |
| [19-RELEASE-CHECKLIST](19-RELEASE-CHECKLIST.md) | Go/no-go gates and handoff | Owner |
| [20-PITCH-DECK](20-PITCH-DECK.md) | 8-slide narrative | Presentation |
| [21-COMPETITIVE-POSITIONING](21-COMPETITIVE-POSITIONING.md) | Competitor differentiation | Product |
| [22-MODEL-EVALUATION](22-MODEL-EVALUATION.md) | LLM selection, evaluation, guardrails | AI engineering |
| [23-PRIVACY-AND-DATA](23-PRIVACY-AND-DATA.md) | Data minimization, privacy and retention | Security |
| [24-OWNER-HANDOFF](24-OWNER-HANDOFF.md) | Publish, initial checks and next owner steps | Owner |

**Normative priority:** official hackathon rules > security policy > API/schema contracts > technical specification > PRD > backlog > marketing copy. On conflict, record an ADR and update affected references. Never retroactively mark planned tests as passed.

## Event interpretation

Official event: https://lablab.ai/ai-hackathons/vultr-hackathon. Main challenge requires Vultr VM-backed orchestration, Vultr Serverless Inference for LLM calls, real code or browser execution in isolated sandboxes, and a recorded containment example. Public demo URL, repository, video, architecture explanation are submission requirements. The event's live dashboard currently lists a cutoff at **2026-11-08 22:00 UTC**. Rules can change; recheck before final submission. Original and MIT-compliant work required.

## Controlled terminology

- **Mission:** a user-defined business objective with immutable input snapshot.
- **Plan:** typed ordered steps proposed by a model and validated against policy.
- **Run:** one attempt to execute a mission; may have multiple bounded sandbox steps.
- **Sandbox:** a disposable constrained runtime for untrusted code/browser actions.
- **Finding:** a structured, evidence-linked exception detected during a mission.
- **Evidence artifact:** immutable file/screenshot/log fragment with digests, origin and traceability.
- **Evidence manifest:** canonical metadata collection signed by the trusted control plane.
- **Verified:** deterministic checks passed; not a statement of absolute security.
- **Approval:** human authorization for a specific proposed action, never a blanket grant.

## Versioning and completion

Specifications are **proposed design v1.0**. Each implementation item must be separately marked done by actual tests and linked commits. Planned P0 work must not be described as shipped until acceptance gates pass.

## New Fabric design addenda (not shipped)

| Doc | Purpose |
|---|---|
| [25-FABRIC-VISION](25-FABRIC-VISION.md) | Product platform vision, product primitives and scope |
| [26-PROOFPACK-DESIGN](26-PROOFPACK-DESIGN.md) | Verifiable receipt semantics and EVP-1 migration caveats |
| [27-ZERO-TRUST-FABRIC](27-ZERO-TRUST-FABRIC.md) | MicroVM decisions, egress, sessions and worker capabilities |
| [28-AMBITION-ROADMAP](28-AMBITION-ROADMAP.md) | Hackathon Tier H/S/P delivery gates and cut rules |
| [29-REVIEW-ACTION-REGISTER](29-REVIEW-ACTION-REGISTER.md) | Open architecture and security review findings |
| [30-CONTAINMENT-THEATER](30-CONTAINMENT-THEATER.md) | Owned-fixture security demo playbook |

These docs supplement but do not silently replace the v1 OpenAPI and EVP-1 schemas; status remains design-only.
