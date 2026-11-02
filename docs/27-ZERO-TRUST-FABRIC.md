# Zero-Trust Execution Fabric

Status: DESIGN ONLY; no penetration test or security certification exists. Protect actual controls, not slogans.

## Trust boundaries
Z0 Public browser: TLS, rate limits, secure HttpOnly SameSite demo session, CSRF/Origin protection on mutations, object-level authorization for mission/run/evidence/approval.
Z1 Vultr VM A: Go API, policy compiler, database, independent verifier, signer and Vultr Inference credentials. No untrusted Python/browser code in its process.
Z2 Vultr VM B: authenticated supervisor holding only narrow worker credentials; private inbound connection from VM A; no Z1 application secrets.
Z3 Guest: disposable untrusted code/browser sandbox with no host mounts, privileged container, Docker socket, secret mounts, host PID namespace or unbounded execution.
Z4 External inference and project-owned mock vendor portal: LLM response and vendor content are DATA, not privileged instructions.

## Runtime selection
Prefer Microsandbox microVM if VM B has usable KVM, supported libkrun and verified network controls; see https://docs.vultr.com/how-to-set-up-agent-sandboxing-on-vultr-cloud-compute. If not, use hardened nonprivileged container on separate VM with seccomp/AppArmor, no-new-privileges, dropped caps, readonly root, scratch tmpfs, cgroup CPU/memory/PID/disk/output/time limits. If isolation cannot be demonstrated, FAIL CLOSED; do not expose arbitrary user code execution.

Important: Vultr's Microsandbox guide shows public outbound internet connectivity can exist by default; microVM isolation does NOT itself provide deny-by-default egress. Use an enforcement gateway outside the guest. Block private, metadata, loopback and link-local IPv4/IPv6 targets; test redirect, DNS rebinding and actual socket destinations.

## Capability model
The trusted compiler creates a single-use, expiring job envelope binding mission/run/session, tool ID, image/code digest, input handles and hashes, resource/egress rules, policy revision, nonce and action permissions. Worker authenticates sender via private mTLS or equivalent proven channel and rejects replay/expiry and unauthorized tool changes. A model cannot mint capabilities. Worker output is never trusted to authorize actions.

## Key and artifact safety
Signing key, database DSN and inference credential stay on VM A. Verify artifact digests from actual bytes. Provide short-lived scoped read-only input access; encrypt and authorize artifacts; no public unauthenticated trace URLs. Separate model explanation from verdict. Protect GitHub Actions write tokens from untrusted code.

## Required negative acceptance tests
1. Loop times out, sandbox destroyed, control plane still responds.
2. Forbidden private/metadata network request denied, with observed proof.
3. Prompt injection in project-owned mock HTML does not grant network/tool privileges.
4. Guest cannot access app/DB/inference/signing credentials or host mounts.
5. Expired/replayed capability denied.
6. Session B cannot read Session A's evidence; CSRF mutation denied.
7. Tampered artifact rejected; wrong monetary result rejected.
8. Worker dies during job; lease reaper prevents permanent RUNNING state.

Run only on project-owned synthetic fixtures, not third-party production. A failed critical gate prevents public launch. Remaining risks include kernel/hypervisor vulnerabilities, control-plane takeover, source deception and misconfiguration; no claim of 100% safety.
