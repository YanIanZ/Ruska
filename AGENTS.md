# RUKSA CHORD — Implementation Instructions

Current scope: Blast Radius Zero, emergent multi-agent coordination failures. **NOT** procurement invoice reconciliation, REA reverse engineering or RELIC legacy software restoration.

Start with docs/PRD.md, docs/ARCHITECTURE.md, docs/SECURITY.md, docs/CHALLENGE-MAPPING.md, and docs/TEST-PLAN.md.

The offline Python engine in chord/ is a safe bounded reference model. It is NOT a sandbox and does NOT make Vultr calls. Implement the next stage as separate Go control VM + disposable isolated worker VM, with all agent model planning/code generation through Vultr Serverless Inference. Model output cannot grant permissions, raise budgets, or decide global safety verification results.

Do not run generated Python in the web/API process. Sandbox restrictions: nonroot, no privileged mounts or Docker socket, no cloud/DB/signing secrets, deny egress by default, CPU/mem/PID/wall-time/output limits, destruction and cleanup proof. Re-check any microVM/KVM assumptions on actual Vultr instance.

Production-like test targets must be synthetic and project-owned. Tests against real external systems require separate explicit authorization; no auto-patching real operations or moving real inventory/funds.

To mark a feature DONE: include actual run ID, commit SHA, tested input, observed trace, measured resource outcome, and negative test status. Never describe locally simulated interleavings as a successful containment drill or Vultr-hosted multiagent execution.

Priority: real sandboxed agent code execution > correct invariant checker > counterexample and patch replay > excellent UI and submission.
