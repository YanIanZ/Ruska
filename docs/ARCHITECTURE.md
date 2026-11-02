# CHORD Architecture — Trusted Control, Untrusted Actors

**Status:** implementation proposal, not deployment evidence.

\`\`\`mermaid
flowchart TD
 U[Operator Web UI] --> API[Go API on Vultr VM A]
 API --> AUTH[Session Authorization]
 API --> PL[Vultr Serverless Inference]
 PL --> POL[Typed Plan and Policy Compiler]
 POL --> DISP[Authenticated Job Dispatcher]
 DISP --> SUP[Worker Supervisor on Vultr VM B]
 subgraph EX[Disposable Sandboxed Run]
  SUP --> ACT[Agent A + Agent B Code]
  ACT --> STATE[Shared Synthetic Inventory]
  STATE --> LOG[Bounded Event Trace]
 end
 LOG --> VER[Trusted Global Invariant Checker]
 VER --> REPLAY[Counterexample Replay + Patch Compare]
 REPLAY --> UI[Collective Safety Report]
\`\`\`

## Two authority boundaries
- **Trusted VM A:** HTTPS frontend and Go control plane, immutable experiment snapshots, policy, trusted verifier, session-bound report storage and Vultr Serverless Inference credentials. Does not run generated agent code.
- **Worker VM B:** private authenticated dispatcher endpoint and disposable nonprivileged containers or microVM guests. Each run receives only bounded input, no DB/API keys, network denied by default and a time-limited capability. Job output is untrusted until independently checked.

## Agent-driven code execution
The model proposes a strictly typed experiment plan and may write Python actor/scheduler code under an allowlisted test harness. Go accepts only recognized tool IDs, bounded step counts, fixed fixture IDs and explicit resource policy. Generated code is executed in an actual disposable sandbox on Vultr VM B, never in VM A. Supervisor records exact source SHA-256, runtime image digest, limits, start/end, exit code and cleanup. Worker traffic must not reach unrelated user missions.

## Independent verification
The trusted checker reconstructs transitions and verifies stock conservation: remaining_stock >= 0 and reservations_issued <= initial_stock. Each claimed failing schedule is accompanied by original trace records and verifiable state evolution. It rejects malformed, incomplete or contradictory traces. A model cannot set VERIFIED. Re-run the same schedule with a typed patch candidate to compare under identical inputs.

## Results transport and lifecycle
Experiment states DRAFT -> PLAN_VALIDATION -> QUEUED -> EXECUTING -> VERIFYING -> NEEDS_REVIEW | COMPLETED | FAILED | BLOCKED. Each event includes run and mission IDs, sequence and timestamp. Idempotency key required for job creation. Worker lease expiry and orphan sweeper reconcile unexpected worker crashes. Side-effect proposals require exact payload digest approval and stay inside synthetic fixtures.

## Web interface
Mission board, shared-state event strip, interactive agent interleaving, minimal counterexample, side-by-side patch evaluation, containment panel and report export. Use actual measurements; no fake logs.

## Isolation stance
Docker is recommended by the event, with microVM/gVisor optional if supported. Rootless containers share a kernel; dedicated VM worker, resource/egress controls and negative tests are mandatory irrespective of runtime. No claim that a microVM alone denies internet access.

## Budget
Avoid Kubernetes and one-VM-per-schedule: deploy Go frontend/API on VM A, execution supervisor on VM B, per-run disposable containers, short-lived results and hard concurrency quota. One worker job enumerates 20 deterministic interleavings rather than provisioning 20 cloud machines.

## Future extension
Other policy templates (task queue retries, cross-agent approvals, shared rate limits) can plug into the invariant contract, without turning RUKSA into a generic reverse engineering tool.
