# CHORD Security Threat Model — Containment First

**Status:** untested design requirements. Zero blast radius is a contest theme, **not** a literal guarantee of zero risk.

## Protected assets
Vultr inference/API keys, signing material, user sessions, report blobs, VM A database, worker supervisor authority and availability. Untrusted elements: user-supplied prompts, generated actor code, model planning output, sandbox stdout/trace, imported configurations and future fixture HTML.

## Primary threats and controls
| Threat | Mitigation | Negative test |
|---|---|---|
| Generated agent code attempts host access | Dedicated VM B, nonprivileged isolated guest, no mounts/Docker socket, no capabilities | Try benign forbidden host file path, denied |
| Unlimited CPU/RAM/PIDs/disk/logs | cgroup controls, wall clock timeout, output caps, cleanup supervisor | Endless loop killed, VM A remains healthy |
| SSRF/exfiltration from worker | No network by default; enforce at host/gateway not text-only URL filter | Controlled forbidden destination denied |
| Model asks for extra tools/privileges | Go typed schema gate and strict tool/fixture allowlist | Unknown tools rejected, no execution |
| Worker forges a safe verdict | VM A verifier independently checks raw state transitions, schema and input digest | Altered trace rejected |
| Session A reads mission B | scoped cookie, CSRF/Origin for mutation, row/artefact authorization | Cross-session 403/404 |
| Worker impersonation/replay | authenticated private dispatcher, one-time capability, nonce, expiry and job digest | expired/replayed job denied |
| Prompt injection in experiment comments | treat model and fixture text as data, not instructions | forged policy instructions ignored |
| Unauthorized real-world effects | sandbox uses synthetic in-memory resource only | no external API calls possible |
| Dependency/supply chain | pinned worker image digest, minimal dependencies, CI read-only token | untrusted dependency cannot run with secret |

## Sandboxing implementation
Minimum per job: fresh guest, nonroot, readonly root FS, scratch tmpfs with quota, no devices/privileged mounts, no Docker socket, blocked outbound network, seccomp/AppArmor where available, memory/PID/CPU/wall-time limits, bounded stdout, kill/teardown, cleanup evidence. No secrets inside sandbox. Serverless Inference calls are made by VM A before dispatch; do NOT call inference from sandbox with API key.

## Proof vs assumption
A successful code execution trace is not proof of safe isolation. A signed receipt is not proof that an output is true. Passing 20 toy schedules does not prove that a distributed system is safe under crashes, network partitions, retries or additional agents. Label security result per tested capability and environment.

## Pre-public go/no-go
- [ ] All real agent code executes outside API process.
- [ ] Host mounts, secrets, network escape and privilege probes are denied.
- [ ] Timeout, OOM and orphan cleanup demonstrated in worker.
- [ ] Session access isolation enforced and tested.
- [ ] Trusted verifier catches tampered trace.
- [ ] Per-session model/run quota and emergency kill switch available.
- [ ] User-facing claims show which tests are NOT_RUN.

## Containment video
Use a harmless synthetic unbounded loop in a disposable sandbox; demonstrate timeout/kill, cleanup and VM A /healthz responding. Do not demonstrate host-destructive commands or use any real third-party system. Record actual logs and timestamps, never fabricated output.
