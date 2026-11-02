# RUKSA Fabric — Ambitious Product Vision

Status: PROPOSED DESIGN, not an implemented service. Challenge: Vultr Agent Rush / Blast Radius Zero.

## North Star
RUKSA is a verifiable autonomous execution fabric: AI proposes work, a deterministic policy compiler authorizes bounded capabilities, isolated runtimes do real work, a trusted verifier checks claims, and users receive a machine-inspectable ProofPack. Human approval gates irreversible actions.

**RUKSA is more than an invoice checker, but procurement remains the first end-to-end vertical slice.** This is a stronger business story than a generic sandbox or a broad unfinished agent platform.

## Three reusable primitives
1. Mission Capsule: immutable input snapshot and digest, typed plan, allowed tools, resource and network budget, expiry, approval requirements and exact policy version. Model text carries no execution authority.
2. Execution Fabric: per-job disposable sandbox on a separate Vultr VM, lifecycle observation, bounded memory/CPU/PIDs/time, optional browser behind strict egress gateway, and observable teardown.
3. ProofPack: input lineage, code/image digest, policy decisions, actual execution receipt, verifier verdict, optional digital signature, reproduced results, and carefully separated assurance flags.

## Signature features
- **Adversarial Twin Lite (Hackathon):** agent-generated Python produces findings; independent trusted Go code computes canonical invoice differences. A fabricated $190 claim must be rejected against the $180 ground truth. Never equate two LLM opinions with independent proof.
- **Containment Theater (Hackathon):** visible, repeatable safety demonstrations on owned synthetic data: runaway execution terminated, forbidden network destination blocked, injected supplier-page instruction denied, control-plane uptime preserved.
- **ProofPack Explorer (Hackathon):** side-by-side agent claim, computed truth, source rows, policy trace and sandbox evidence, with explicit UNKNOWN / NOT_RUN / UNSIGNED states.
- **Shadow Replay (Stretch):** re-execute selected computations in a second clean sandbox, mark divergent findings INCONCLUSIVE. It supplements—not replaces—trusted deterministic checks.
- **Policy Studio & SDK (Post-event):** signed reusable mission capsules, strict connector contracts, approvals, multi-tenant permissions, verifiable worker fleet and external system integrations.

## First user journey
Operator chooses synthetic 150 invoice / 150 PO fixture; Vultr inference proposes plan; Go policy compiler constrains it; Python sandbox executes actual reconciliation; verifier independently confirms three seeded exception types and $180 variance; user inspects ProofPack; operator approves a vendor clarification DRAFT. No payment, vendor email or third-party transaction is sent.

## Value proposition
RUKSA makes agent output accountable by separating **execution observed**, **integrity verified**, **business-rule verified**, and **source authenticated**. None implies complete immunity to attack or that external sources are truthful. A signed record proves bytes relative to signer trust, not global truth.

## Long-term market
Procurement is the beachhead. The same protocol could later support engineering QA, policy-bound research and operational audits. Those industries, real integrations, SSO, compliance and global fleet scaling are roadmap ideas—not six-day deliverables.

## Goal measurement
Record actual result accuracy on synthetic fixture, negative security-test pass rate, evidence coverage for verified findings, task completion latency, model cost and reviewer time. Never publish made-up security percentages or runtime benchmarks.
