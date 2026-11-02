# RUKSA RELIC — Documentation Index
**Active product 2026-11-03:** Autonomous Digital Restoration Studio. **Status:** design only.

## Authoritative current scope
| File | Coverage |
|---|---|
| [31 Vision](31-RELIC-PRODUCT-VISION.md) | Product identity and originality |
| [32 PRD](32-RELIC-PRD.md) | Requirements and acceptance |
| [33 Architecture](33-RELIC-ARCHITECTURE.md) | Control/worker trust boundaries |
| [34 Behavior Genome](34-RELIC-BEHAVIOR-GENOME.md) | Behavioral contracts and unknowns |
| [35 Roadmap](35-RELIC-ROADMAP.md) | Six-day build priorities |
| [36 Security](36-RELIC-SECURITY.md) | Sandbox, authorization, privacy, IP |
| [37 Demo](37-RELIC-DEMO-PITCH.md) | Recorded demonstration and story |
| [38 Competition](38-RELIC-COMPETITIVE-THESIS.md) | Adjacent work, positioning |
| [39 Tests](39-RELIC-TEST-PLAN.md) | Functional and containment acceptance |
| [40 Data/API](40-RELIC-DATA-AND-API.md) | New restoration schema and endpoints |
| [41 UX](41-RELIC-UX.md) | Fossil viewer, before/after, parity arena |

Machine contracts: [genome JSON Schema](../schemas/behavior-genome.schema.json), [RELIC OpenAPI](../schemas/relic-openapi.yaml).

## Superseded
Documents 01–30, schemas/openapi.yaml, old procurement fixtures and earlier Fabric design are **historical**, not current instructions. Current RELIC 31–41 takes precedence. We deliberately do not remove Git history. If any older document conflicts with the RELIC PRD, ignore older requirements for implementation.

No features, integration/security tests, or Vultr deployment have been verified as shipped. Official hackathon rules override all docs: https://lablab.ai/ai-hackathons/vultr-hackathon

## RELIC 2.0 depth addenda — design

| File | Role |
|---|---|
| [42 — Continuity Engineering](42-RELIC-2-0-NORTH-STAR.md) | Product innovation and niche |
| [43 — Counterfactual Archaeology](43-COUNTERFACTUAL-ARCHAEOLOGY.md) | Safe behavior discovery and probe search |
| [44 — Continuity Passport](44-CONTINUITY-PASSPORT.md) | Exportable executable proof with assurance labels |
| [45 — Demo Amplifier](45-DEMO-AMPLIFIER.md) | Show-before/after plus regression detection |
| [46 — Delivery Scorecard](46-RELIC-DELIVERY-SCORECARD.md) | Scope, daily checkpoints and go/no-go |

The code in [examples/relic-lab](../examples/relic-lab/README.md) is an **offline synthetic model-parity prototype**, not the real browser + AI product. Documents 31–41 remain the foundational RELIC architecture; 42–46 add design depth without changing its target use case.
