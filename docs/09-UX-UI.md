# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# UX/UI Specification — Evidence-Centered Operations

## Product voice and identity

**Brand:** RUKSA · **Tagline:** Work Done. Proof Attached. · **Design intent:** sober, credible, fast, accessible operational workspace. Do not resemble a generic chatting interface with fake tool animations. Color is a secondary indicator, not the sole bearer of safety state.

## Information architecture

```text
Dashboard
├── Missions
│   ├── New Mission (objective + fixture/upload)
│   └── Mission Detail
│       ├── Plan & policy gate
│       ├── Execution timeline (SSE)
│       ├── Findings & evidence
│       └── Proposed Actions / approval
├── Evidence Explorer (filtered per mission)
├── Containment Monitor (per run)
└── Settings / About / Demo limitations
```

## Screens and interaction contracts

### S01 Dashboard

Cards: missions processed, findings needing review, verified price variance (separate from suspected duplicate exposure), safety incidents. List latest missions with clear state and date. Primary CTA `New Mission`. Empty state offers the synthetic fixture; do not fabricate completed runs.

### S02 New Mission

Fields: title, task objective, dataset selector (`demo-2026-11-v1`), optional known vendor-demo URL. Before launch show file count/row count, supported data classes, privacy reminder and credit/cost disclaimer. The action `Start safe run` first requests a plan, confirms policy profile and never causes a business side effect.

### S03 Execution Workspace

Three-column desktop: plan timeline, live safe event feed, resource/containment summary. Mobile stacks these in document order. Visually distinguish `plan proposed`, `code actually executed`, `verification complete`. Show real step timestamps and sandbox ID from backend; never synthesize logs. Include accessible pause/cancel controls only when backend can fulfill them.

### S04 Finding Detail / Evidence Explorer

Headline with finding class and monetary amount (if applicable), source comparison, confidence/verification labels, source row anchor, verifier rule and input checksum. A tabbed drawer shows screenshot, sanitized code/exit metadata and manifest integrity status. For missing evidence, show `INCONCLUSIVE` and explanation. Add export buttons only when corresponding endpoints exist.

### S05 Approval Center

Displays exact proposed draft and digest, consequence statement (`No external email sent in MVP`), approve/reject buttons and confirmation. Re-review required if payload changes. Never auto-approve on page load or timeout.

### S06 Containment Monitor

Show sandbox lifecycle, permitted URLs, CPU and memory caps, time limit, termination reason, cleanup recorded. Demonstrate a test infinite loop ending with `TIMED_OUT`, not an untested security claim. Worker host identifiers should be redacted from public demo.

## Design system

- **Colors:** neutral charcoal/slate surfaces, blue information, amber review-needed, red blocked/failed, green verified only after checks. Provide high contrast light/dark themes if time permits.
- **Typography:** readable body >= 14–16px, tabular digits for money and hashes, never rely on tiny tables.
- **Spacing:** 8px scale, responsive grids; action group remains visible on narrow widths.
- **Icons:** informative only with accompanying text, not icon-only status.
- **Microcopy:** prefer `Price mismatch detected` over `AI found fraud`; `Verification passed` over `100% secure`.

## Accessibility standards

Target WCAG 2.2 AA where practical: keyboard focus and logical order, visible focus indicator, labeled upload and form controls, text alternatives for status icons and screenshots, sufficient contrast, non-color-only state, `aria-live` only for meaningful SSE changes (avoid announcing every token), reduced-motion support, modal focus management, error messages associated with fields, and table headers for financial comparisons. Avoid overwhelming animation in safety dashboard.

## UX acceptance criteria

1. A new user completes a fixture mission without knowing shell/Docker.
2. Every `VERIFIED` financial result can be traced to invoice+PO in <=3 interactions.
3. `NEEDS_REVIEW`, `BLOCKED` and `FAILED` states have actionable copy.
4. A keyboard-only tester can inspect evidence and approve a draft.
5. Browser refresh recovers mission state from API, not local component memory.
6. The UI never presents unimplemented features as functioning buttons.

## Copy examples

- `Run is constrained to 60 seconds and synthetic vendor resources.`
- `This finding is verified against the current uploaded reference data; it does not prove a payment was made.`
- `Draft approved for export. No external communication has been sent.`
- `Sandbox timed out and was destroyed. The control plane remained responsive during this test.` (only if measured and supported)
