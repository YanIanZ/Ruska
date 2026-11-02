# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# Security Threat Model — Blast Radius Zero

**Security stance:** defense-in-depth and explicit limits. **Not a guarantee of zero vulnerability.** Threat model must be revisited before public arbitrary-code execution.

## Assets and attackers

Protected assets: Vultr inference/API credentials, evidence signing key, database connection, private control-plane files, other user sessions, infrastructure availability and the integrity of findings. Attackers: anonymous internet clients, a malicious CSV/HTML supplier page, prompt injection embedded in an invoice, runaway generated code, a compromised sandbox process, and accidental operator misuse.

## Attack surface and controls

| ID | Threat | Preventive control | Test / evidence |
|---|---|---|---|
| T01 | Agent prompt injection in supplier HTML/CSV | Treat retrieved content as untrusted data; typed plan and strict tool allowlist | malicious DOM instruction does not change tool authority |
| T02 | Generated code reads environment/API keys | No secrets, cloud metadata or host mounts in sandbox | attempt to read key returns unavailable; prove without exposing secrets |
| T03 | Infinite loop / CPU exhaustion | cgroup CPU, memory, PIDs and wall-time limit; kill job and cleanup | bounded loop test terminates within policy tolerance |
| T04 | Path traversal / filesystem damage | read-only rootfs, tmpfs workdir, no privileged mounts | attempted read/write outside workspace denied |
| T05 | SSRF to metadata/internal services | DNS/IP allowlist, restricted egress, redirect revalidation | deny metadata, localhost, private/link-local destinations |
| T06 | Container escape | least privilege, rootless where supported, seccomp/AppArmor, no Docker socket, dedicated worker VM | configuration audit; acknowledge shared kernel residual risk |
| T07 | Worker impersonation/result spoofing | mTLS or strong signed short-lived envelope + digest validation | altered nonce/token rejected |
| T08 | Evidence tampering | SHA-256 content addressing, trusted verifier, signed manifest | change artifact byte -> signature/hash verification fails |
| T09 | Cross-session data access | session scope in query filters, resource authorization checks | different demo session gets 404/403 |
| T10 | Sandbox log injection | structured logging, escape output in UI, truncate and sanitize | malicious ANSI/HTML displayed as text |
| T11 | Unbounded model cost | token caps, daily quota, throttling, max plan steps and retries | budget exceeded -> explicit BLOCKED state |
| T12 | Arbitrary workflow side effects | read-only MVP, scoped approval digest for export only | agent cannot send emails or spend funds |
| T13 | CSV formula injection | escape spreadsheet formula-prefixed cells in exported CSV | malicious export inert on spreadsheet open |
| T14 | Artifact overflow/storage DOS | upload cap, output cap, screenshot cap, TTL cleanup | oversize job stopped, no uncontrolled disk usage |

## Isolation requirements

1. **Control/worker split:** untrusted code never runs inside Go API or database host process.
2. **No host access:** worker containers nonprivileged; no `--privileged`, `--network=host`, Docker API socket, device mounts, control-plane volumes or host PID namespace.
3. **Filesystem:** readonly root filesystem, single scratch tmpfs, nonroot UID/GID, no secret mounts.
4. **Resources:** explicit CPU and memory limits, `pids-limit`, no-new-privileges, cap-drop=ALL, wall clock timeout, capped stdout/stderr and artifact total size.
5. **Network:** Python sandbox egress denied by default; Playwright only reaches controlled vendor-demo host(s) using a deny-by-default network gateway. DNS rebinding and redirects must not bypass restrictions. Where runtime cannot enforce destination restrictions robustly, disable browser automation in public demo until it can.
6. **Lifetime:** new disposable sandbox per step; supervisor records cleanup; periodic orphan sweeper on VM B.
7. **Secrets:** only control VM stores Vultr Serverless Inference credentials and evidence signing material. Worker receives short-lived capability limited to one job and only its approved sanitized input.
8. **Public demo:** rate limiting and session quota. Restrict general-purpose code-entry for anonymous users; expose controlled sample missions only until adversarial testing passes.

## Containment evidence scenario

**Safe example:** agent-generated `while True: pass` executed in test-only sandbox with timeout set to 5 seconds. The supervisor records limit, observed wall time, termination reason `TIMEOUT`, container teardown, and unrelated control-plane request latency. Video shows evidence without leaking the worker host or credentials. A second scenario uses a mock vendor page containing prompt-injection text asking the agent to ignore policy. Show a denied tool request or unchanged plan.

**Do not** demonstrate attacks against real vendor sites or real users; all targets are project-owned fixtures.

## Failure modes and residual risk

Container isolation shares host kernel; kernel-level vulnerabilities remain possible. VM B reduces effect on control plane but does not eliminate cloud provider risk. Signed manifest gives byte-level integrity and signer authenticity only while signing key stays trustworthy; it cannot establish that all business facts are correct. Browser screenshot alone does not prove DOM authenticity; source origin, timestamp and normalized content hash are also captured.

## Incident response (prototype)

1. Disable public run creation; preserve sanitized metadata and run IDs.
2. Revoke inference and worker credentials; rotate signer after incident.
3. Destroy affected sandbox/worker VM if compromise suspected.
4. Audit stored evidence for secret leakage; remove public logs and affected links.
5. Restore with hardened image and new keys; document and retest before resuming public demonstration.

## Pre-launch security gate

- [ ] No hardcoded secrets, leaked `.env` or provider tokens.
- [ ] Policy rejects unknown tools, URLs and destinations.
- [ ] Docker/worker rootless or least-privileged config inspected.
- [ ] Worker has no DB or cloud credentials.
- [ ] Timeout, OOM and cleanup tests passed.
- [ ] Cross-session access rejected.
- [ ] CSP, safe headers, TLS and rate limiting enabled.
- [ ] Failed containment tests visibly block release.
