# Technical Architecture — RUKSA RELIC

Status: DESIGN ONLY. Vultr Challenge 1 requires Vultr VM backend, Vultr Serverless Inference, isolated actual code/browser execution, public web UI and containment video.

## System topology
\`\`\`mermaid
flowchart TD
  User[Owner browser] --> Web[Next.js Restoration Studio / Vultr VM A]
  Web --> API[Go API and session auth]
  API --> Pg[(PostgreSQL run states and traces)]
  API --> Infer[Vultr Serverless Inference]
  API --> Policy[Typed job policy compiler]
  Policy --> Dispatch[Authenticated private dispatch]
  subgraph Worker[Vultr VM B / execution trust zone]
    Dispatch --> Supervisor[Disposable runtime supervisor]
    Supervisor --> Browser1[Playwright Legacy Observer]
    Supervisor --> Builder[Code Generation Build Sandbox]
    Supervisor --> Browser2[Playwright Paired Parity Test]
  end
  Browser1 --> Genome[Observed Behavior Genome]
  Builder --> Artifacts[Generated Source Artifact]
  Browser2 --> Parity[Trusted Contract Comparator]
  Genome --> Parity
  Artifacts --> Parity
  Parity --> Capsule[Revival Capsule for human review]
\`\`\`

## Execution principles
- User authorization and allowed demo domains enforced at API. The model cannot create network privileges.
- Browser steps are restricted to a project-owned mock portal; isolated disposable fixture database enables safe repeated test submissions.
- Browser observer collects sanitized state/action/response pairs. Avoid raw secrets, cookies, full HAR with private tokens, or exposed infrastructure headers.
- Model is a **hypothesis generator**, not the ground-truth oracle. It may propose field mapping and new UI code, but confidence remains bounded to what was observed.
- Compiler emits a typed Behavior Genome. Human must confirm ambiguity before code generation.
- Candidate code is built in a worker guest, no execution on VM A; output is untrusted until integrity and parity checks pass.
- A **trusted comparator** normalizes cases from independent fixture truth and compares outcomes produced by both executables.
- Signatures are optional until key lifecycle and byte-level verification are tested. Distinguish signed integrity and behavioral parity.

## Worker runtime
Use separate Vultr VM B. Prefer Microsandbox microVM when /dev/kvm and explicit outbound network enforcement are confirmed. Fallback hardened nonprivileged container with readonly root, tmpfs workdir, seccomp/AppArmor, no-new-privileges, all capabilities dropped, no Docker socket, memory/CPU/PIDs/time/output caps. Browser is not allowed unrestricted egress.

## Data flow
1. Operator creates restoration mission referencing pre-registered owned fixture.
2. Go generates scoped capability: session, mission, allowed tool and domain, max steps, max wall clock, source digest, expiry and nonce.
3. Observer browser explores bounded paths and submits trace. Trace is untrusted until validated and bound to original fixture origin.
4. Vultr Inference proposes normalized Behavior Genome; separate deterministic parser validates supported fields and observed tags.
5. Operator accepts/corrects Genome; model generates bounded TypeScript/HTML form code template based on approved schema.
6. Build worker installs pinned dependencies and executes actual build; preview is isolated and cannot write to legacy service.
7. Parity runners use matched synthetic inputs and collect outcomes, errors, navigation transitions.
8. Trusted comparator produces PASS/FAIL/NOT_TESTED; user gets interactive diff and exportable migration capsule.

## Stronger IP & safety boundary
Prototype accepts ONLY our own synthetic site. Production extension requires site-owner written permission and terms review. Do not copy styling, logos, content, proprietary frontend code or bypass access controls. Reconstruct allowed behavior/intent into original code only.

## Reliability
Run ID and generation attempt ID are immutable. Retries bounded. Unknown or unsupported workflow elements are not silently marked passed. Outbox and lease expiry prevent stranded jobs. All artifact fetches require owner-session auth. Never put Vultr credentials, signer keys or database DSNs into sandbox or frontend.

## Failure examples
- Generated UI passes screenshot similarity but wrong validation -> PARITY FAILED.
- Agent guesses inaccessible backend logic -> HYPOTHESIS / UNKNOWN, requires owner review.
- Sandbox tries network destination outside controlled fixture -> BLOCKED and recorded.
- Browser/script loops -> timeout and worker teardown, no stale success.
