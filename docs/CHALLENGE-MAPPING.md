# Official Vultr Agent Rush Mapping — CHORD Challenge 1

**Primary track: Blast Radius Zero**. This is NOT a Future of Work track submission, though coordinated-agent reliability may have future enterprise value.

Official pages:
- https://lablab.ai/ai-hackathons/vultr-hackathon
- https://community.vultr.com/e/vultr-agent-rush-hackathon

## Challenge 1 mapping
| Official requirement | CHORD implementation target | Status |
|---|---|---|
| Production-style web app | Real mission, trace, replay, patch comparison, report UX | PLANNED |
| Vultr VM backend central control | Go API/orchestrator on Vultr Compute VM A | PLANNED |
| All agent LLM calls on Vultr Serverless Inference | Typed experiment planner and Python actor-code authoring with endpoint https://api.vultrinference.com/v1 | PLANNED |
| Pattern A: model writes code, sandbox runs | Model-authored bounded test code executed in fresh container on Vultr worker VM B | PLANNED |
| Multi-step agentic workflow | Objective -> plan -> policy -> code -> execute -> verify -> propose patch -> replay -> report | PLANNED |
| Verifiable actual output | Trusted checker against raw trace + digests + specific schedule and invariant | PARTIAL LOCAL PROTOTYPE ONLY |
| Containment safety | Worker isolation, no keys, time/mem/network limits, guest destruction | PLANNED |
| Public demo URL | HTTPS app running on Vultr | PLANNED |
| GitHub and setup docs | Repo, real install/run/deployment instructions after integration | DOCS AVAILABLE |
| Video including one containment moment | Runaway synthetic process killed, cleanup and healthy API observed | PLANNED |

## Hard boundary between "research prototype" and submission
The local Python schedule enumerator executes a deterministic in-memory model and unit tests. It is *not* Vultr-hosted, an LLM agent, or isolation evidence. A submission may not claim compliance until genuine VMs/inference/worker execution and recorded containment exist.

## Differentiation against sample directions
Unlike generic CSV analysts, code reviewers or site QA sweeps, CHORD tests **global failure invariants produced by interacting agents**. The execution itself remains Pattern A: real model-generated Python runs in a disposable sandbox. The business result is a reproducible collective safety counterexample and controlled coordination repair.

## Judging priorities
Application of Technology: model-to-run-to-verifier loop really works. Presentation: clear six-step inventory race visual and containment. Business Value: reduce risk in multi-agent business automation staging. Originality: focus on finding minimal emergent failure, not claiming model checking was invented.

## Dates
Official online phase Nov 3–8, 2026; verify exact submission cutoff in lablab dashboard. The event specifies public GitHub, web URL, video and architecture. Claim $200 free Vultr credits only after account eligibility and redemption are confirmed.
