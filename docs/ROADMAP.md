# CHORD Execution Roadmap — November 3–8, 2026

**Objective:** deliver one excellent end-to-end experiment + real sandbox containment rather than five incomplete use cases.

| Date | Deliverable | Non-negotiable exit gate |
|---|---|---|
| Nov 3 | Clean CHORD branch, signed-off scope, offline bounded fixture, provision Vultr VM A/B and inference | Main fixture reproducible; Vultr resources reachable |
| Nov 4 | Go plan/control API and worker container on VM B | Real generated Python executed in worker, timeout confirmed |
| Nov 5 | Typed experiment tool, inventory race and trusted invariant verifier | Real 20 interleavings and violating schedule reported |
| Nov 6 | AI-recommended atomic patch, safe replay and denial tests | Wrong policy visibly violates; approved mitigation passes model |
| Nov 7 | Web Mission Studio, trace visualization and report export | Fresh user can run workflow, see evidence, no secret exposure |
| Nov 8 | Repeatable E2E, containment video, README architecture and submission | Public URL and live recorded execution, official lablab entry |

## Required P0
Vultr VM backend, Serverless Inference calls, actual isolated code execution and cleanup, deterministic verifier, one cross-agent emergent failure trace, a checked patch, public UX, GitHub and video.

## Optional P1
More agent fixtures, differential schedule search, browser pattern B, live coordination metrics, Ed25519 signed report, microVM backend if compatible and time permits.

## Post-event P2
B2B staging connectors, remote policy import, richer timing/network fault model, customer-owned credential access via least privilege, multi-tenancy and reproducible regression suites.

## Cut rules
If real sandbox not working by Nov 4, drop UI sophistication and focus execution boundary. If Vultr inference not available, disclose blocker; do not silently substitute another model provider for official Challenge 1. If verifier not correct, pause new scenarios. If network/secret/time controls fail, disable public run creation; do not misrepresent unsafe worker as contained. Do not expand into "Future of Work" generic workflows while CHORD's minimum is unshipped.

## Submission checklist
- [ ] Official team/track registration and eligibility.
- [ ] Vultr VM deployment and actual Serverless Inference model ID.
- [ ] Real sandbox run with logs/measurement.
- [ ] Public working web UI and GitHub docs.
- [ ] Containment moment with real process termination.
- [ ] Video, architecture explanation, source and test instructions.
- [ ] Owner review, final link and official lablab submission before cutoff.
