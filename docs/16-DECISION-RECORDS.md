# Architecture Decision Records (ADRs)

**Format:** ADR-ID, Status, Date, Context, Decision, Consequences. Every reversal requires new ADR and update of dependent docs.

## ADR-001 — Go control plane; Python execution workers

- **Status:** Proposed · **Date:** 2026-11-02.
- **Context:** Need a small, predictable orchestrator with concurrency, simple deployment and robust event streaming, while data-analysis libraries run in Python.
- **Decision:** Use Go for API/state/policy/verification and Python only for isolated analysis runtime.
- **Consequences:** Two-language stack and typed job contract; separation discourages accidental code execution inside API. Go is not presumed faster for all workloads.

## ADR-002 — Evidence verification independent of LLM

- **Status:** Proposed.
- **Context:** LLM narratives can hallucinate arithmetic and source citations.
- **Decision:** Financial results must be checked with deterministic integer-cent rules against canonical input snapshots. Model explanations are display-only.
- **Consequences:** Restricted first domain but stronger correctness claim. Verifier rules become versioned auditable code.

## ADR-003 — Separate worker VM

- **Status:** Proposed.
- **Context:** Model-generated code is untrusted, including if model is under our control.
- **Decision:** Place disposable sandbox containers on a separate Vultr worker VM isolated from API/database/inference keys.
- **Consequences:** Higher cost and operational overhead; controls mitigate but do not eliminate kernel escape risk.

## ADR-004 — Do not auto-send or auto-pay

- **Status:** Accepted for MVP scope.
- **Context:** External actions can have irreversible effects or create data exposure.
- **Decision:** Version 1 supports generating and reviewing drafts only; any external vendor communication or financial action is out of scope.
- **Consequences:** Safe, demonstrable approval UX; no claim of automated resolution in real procurement systems.

## ADR-005 — Synthetic fixtures as canonical ground truth

- **Status:** Accepted for hackathon planning.
- **Context:** Real procurement data may contain sensitive financial records, and a reliable demo needs known reference answers.
- **Decision:** Use deterministic synthetic 150-invoice fixture with exactly three anomaly cases and a known $180 price variance.
- **Consequences:** Reproducible tests, but no external validity/generalization claims.

## ADR-006 — Blast Radius Zero as primary challenge

- **Status:** Proposed for official registration.
- **Context:** Product blends safety and procurement; event asks teams to choose one track.
- **Decision:** Enter Blast Radius Zero; foreground real execution and containment as technological differentiators, procurement as business value.
- **Consequences:** Vultr Serverless Inference required for all agent LLM calls. Browser sandbox optional, code sandbox mandatory in chosen implementation plan.

## ADR-007 — Model-agnostic, Vultr-specific adapter

- **Status:** Proposed.
- **Context:** Live model catalog may change during hackathon.
- **Decision:** Configuration selects a tested Vultr Inference model via OpenAI-compatible adapter, with JSON schema validation and retry budget. No other LLM provider for official agent flow.
- **Consequences:** Better portability, but must re-evaluate model reliability and available features after selection.

## ADR-008 — Explicit no-password public demo

- **Status:** Proposed.
- **Context:** A public hackathon URL must be usable but anonymous unbounded code execution is dangerous.
- **Decision:** Signed short-lived demo sessions, per-session quotas, fixed sample mission and strict sandbox policy; no full customer account system during event.
- **Consequences:** Accessible demo with constrained feature set and protected compute budget.

## ADR-009 — Reusable Fabric, narrow hackathon vertical slice
- **Status:** Proposed; date 2026-11-03.
- **Decision:** Mission Capsule/ProofPack are general primitives, procurement remains sole required shipped workflow.

## ADR-010 — Conditional microVM worker
- **Status:** Proposed.
- **Decision:** Prefer Microsandbox if Vultr KVM and independent egress restrictions are validated, else hardened VM-isolated container with truthful risk disclosure.

## ADR-011 — Verifier authority
- **Status:** Proposed.
- **Decision:** Deterministic trusted Go recomputation is authoritative; optional shadow replay only raises inconsistency signals.

## ADR-012 — Distinguish integrity, truth and containment
- **Status:** Proposed.
- **Decision:** Never collapse signed bytes, valid business result, source authenticity and runtime containment into one verified badge.
