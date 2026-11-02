# RUKSA RELIC — Security and Authorization

Status: proposed controls, not a completed security audit.

## Main new threats
1. **Unauthorized cloning / IP:** Restrict public exploration to a site authored and hosted by RUKSA. Require documented owner consent before future arbitrary target URLs. No anti-bot/captcha bypass, token harvesting, copy of protected content or brand identity.
2. **Data privacy:** Synthetic-only prototype, no real names/addresses/identifiers; redact browser traces, HAR, local/session storage, cookies and screenshots; every artifact session-scoped.
3. **Browser SSRF:** Browser egress via independently enforced proxy; deny metadata, link-local, localhost and private net except explicitly isolated owned mock service. Resolve/check every redirect and connection destination, support IPv6.
4. **Untrusted generated code / dependencies:** Generated frontend code is never executed on Go control host; pinned build templates, no arbitrary package downloads or shell tool, sandbox limits and scanned/approved dependencies.
5. **Prompt injection:** HTML/DOM contents are data. An instruction from an old page cannot add tools, make external network calls, read secrets or override the user/owner's approvals.
6. **Behavioral deception:** Visible page may not reflect actual server behavior. Label OBSERVED vs INFERRED vs UNKNOWN and require independent fixture oracle. A screenshot/LLM summary is not test coverage.
7. **Session and CSRF:** Issued expiring sessions, HttpOnly Secure SameSite cookie, CSRF/Origin validation for state mutation; object-level auth for mission, trace, bundle, preview and approvals. No unauthenticated artifact URLs.
8. **Supply chain:** Minimal GitHub CI permissions, pinned images/dependencies, signed reviewed releases where feasible, no untrusted PR jobs with write credentials.

## Runtime requirements
Dedicated Vultr worker VM separated from inference/DB/secrets host; disposable nonprivileged microVM (if KVM supported) or hardened container fallback. No host mounts, no Docker socket, no execution credentials, resource caps, deny-by-default network gateway and teardown. The signing key never reaches guest.

## Tests
- Anonymous request for arbitrary website => denied.
- Expired job capability or replay => denied.
- Guest attempts outbound private/metadata URL => network-enforced deny, no leak.
- HTML prompt injection cannot request new capabilities.
- Infinite loop safely times out with resource cleanup and control-plane health.
- JS injection input does not execute in preview or evidence viewer.
- Cross-session trace retrieval and approval mutation denied.
- Parity result mismatch or missing testcase => not RESTORED.
- Misleading signature/claim => UI displays integrity and coverage separately.

## Release conditions
Critical security tests must pass for public runner. Any new ability to explore third-party systems needs product, legal, privacy and security review; not part of hackathon.

## Limitation honesty
No static HTML + screenshot can reconstruct private backend semantics. No 100% parity beyond test coverage. No "unhackable sandbox" or formal WCAG certification based solely on automated tests.

## Counterfactual probing additional threat boundaries

The probe chooser is not authorized to discover arbitrary web services. It may choose **only** safe typed mutations to registered form inputs on an owner-authored synthetic target. Enforce a per-mission budget (actions, wall clock, network requests, output bytes), server-side egress policy and disposable fixture reset. Treat generated probes as untrusted until approved by deterministic policy; do not infer consent or authorization from an LLM-generated plan. Never send probes to real government or institutional portals without separate explicit owner authorization.

Differential findings can be misleading when the original application has nondeterministic timestamps, session-dependent behavior or inaccessible server-side rules. Normalize known volatile fields only; label uncertainty instead of ignoring divergences. Offline handwritten reference models are not browser-captured original truth.
