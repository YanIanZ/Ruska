# Product Requirements Document — RUKSA 1.0

**Status:** Draft for implementation · **Owner:** YanIanZ · **Launch target:** Nov 8, 2026 · **Challenge:** Blast Radius Zero.

## 1. Executive overview

RUKSA is an autonomous procurement operations tool with a novel product promise: **work is only accepted when the execution and results have attached evidence**. Version 1.0 takes synthetic invoices and purchase orders, plans reconciliation work using Vultr Serverless Inference, executes analysis code inside isolated sandboxes, optionally validates a known synthetic vendor portal through Playwright, verifies arithmetic independently, and generates reviewable findings with reproducible evidence.

## 2. Customer problem and opportunity

Procurement/finance analysts manually move between spreadsheets, vendor portals and approvals. Generic LLMs can summarize but cannot reliably prove that they ran the work or used the right sources. The immediate problem is not lack of answers: it is **lack of accountable, verifiable execution**. Reviewers need to know where each finding came from, what was actually executed, and which actions remain blocked pending human approval.

### Personas

- **Procurement operations analyst:** 20–500 monthly invoices; wants price/PO exceptions and a review queue.
- **Finance controller:** wants audit evidence before approving corrective actions; prefers deterministic numbers and immutability.
- **Security/IT reviewer:** wants proof that untrusted content, model outputs and code cannot access app secrets or unrestricted networks.
- **Hackathon judge:** expects a clear, live, multi-step working agent and one observable containment demonstration.

### Jobs to be done

1. When supplier invoices arrive, compare them with expected prices and PO references so I can detect exceptions without manually reading every record.
2. When AI flags an anomaly, show me the exact input, execution, calculation and evidence so I can make an informed decision.
3. When the AI runs code or browses, isolate its effects so it cannot compromise the business system.
4. When a corrective action is proposed, present it for explicit approval instead of performing irreversible changes.

## 3. Product principles

- **Evidence > eloquence:** no ungrounded verified status.
- **Read-first, act-later:** no external side effects in MVP.
- **Contained by default:** all model-generated code executes outside the application process.
- **Deterministic where possible:** currency and document matching rules are conventional code, not LLM reasoning.
- **Honest failure:** blocked, inconclusive or missing-source states are first-class outcomes.
- **Accessible UX:** findings interpretable without security-domain jargon.

## 4. Functional requirements

| ID | Requirement | Priority | Acceptance |
|---|---|---|---|
| FR-001 | Create mission with file uploads and clear objective | P0 | Mission ID, input checksum and status returned |
| FR-002 | Validate type, size, currency, columns and file safety | P0 | Invalid inputs rejected with field-specific errors |
| FR-003 | Generate typed plan through Vultr inference | P0 | JSON-schema-validated plan with allowed steps only |
| FR-004 | Enforce policy gate before dispatch | P0 | Unsafe plan rejected; no sandbox created |
| FR-005 | Execute generated Python in disposable sandbox | P0 | Actual result, stdout/stderr summary and exit code returned |
| FR-006 | Run Playwright against allowlisted demo vendor portal | P1 | Screenshots + extracted values returned through isolated browser |
| FR-007 | Identify price mismatch, duplicate supplier invoice, unknown PO | P0 | Matches fixture truth set: 3 planted exceptions |
| FR-008 | Independently verify price arithmetic in integer cents | P0 | Exactly +18000 cents for reference price anomaly |
| FR-009 | Bind each verified finding to source evidence | P0 | Evidence links resolve, hashes verify |
| FR-010 | Show live mission progression and containment metadata | P0 | Client sees state transitions via SSE with reconnect |
| FR-011 | Create corrective-action draft and require explicit approval | P0 | No financial mutation or external send in MVP |
| FR-012 | Export human report + machine manifest | P1 | Downloaded artifacts contain trace IDs and statuses |
| FR-013 | Replay an immutable input snapshot | P1 | New run references same input version |
| FR-014 | Organization billing and ERP integration | P2 | Deferred after event |

### Mission acceptance

A mission is `COMPLETED` only after all mandatory steps have terminal successful outcomes, verifier status is consistent, and no critical block remains. A mission with unresolved decisions may be `NEEDS_REVIEW`; it may contain verified findings but never imply approval.

### Anomaly definitions

- **Price variance:** same PO line and SKU, invoice unit price exceeds approved PO unit price; `difference_cents = (invoice_unit_cents - po_unit_cents) * invoice_quantity`. Do not compare floating-point currency.
- **Duplicate invoice:** repeat `(vendor_id, supplier_invoice_number)` across distinct records. Flag both record IDs or produce one pair-level finding with both citations; avoid automatically declaring fraud.
- **Unknown PO:** invoice's PO reference is absent from imported purchase orders. Flag as unverified, not automatically a financial discrepancy.
- Quantity mismatches can be P1 unless demo time permits, to protect P0.

## 5. Nonfunctional requirements (targets, not claims)

| ID | Objective | Target / method |
|---|---|---|
| NFR-01 | Safety | No control-plane secrets mounted in sandbox; negative test |
| NFR-02 | Isolation | Separate worker VM; rootless disposable containers; no host filesystem mount |
| NFR-03 | Limits | Explicit per-job CPU, memory, PIDs, network, output and 60-second wall timeout (tunable) |
| NFR-04 | Correctness | 150-case synthetic dataset reproduces 3 seeded anomalies |
| NFR-05 | UX | Mission status and helpful errors without browser refresh |
| NFR-06 | Availability | Live demo sustains three consecutive E2E runs without manual reset |
| NFR-07 | Traceability | Every verified finding references a source row and verifier result |
| NFR-08 | Accessibility | Keyboard-driven review, visible focus, color-independent status |
| NFR-09 | Security logging | No credentials, raw personal data or complete unsafe code in public logs |
| NFR-10 | Cost | Track VM + inference spend against $200 event credits; no claims of free use |

## 6. Out of scope for event release

Real banking integrations, payments, invoice approval/payout, automatic email sending, production customer PII, universal ERP connectors, accounts/multitenancy, ML training/fine-tuning, persistent arbitrary agent memory, unsandboxed shell execution, general-purpose browsing beyond controlled allowlist, unverified hallucination-based verification.

## 7. MVP user journey

**Start mission → Upload sanitized sample → Review agent plan → Start constrained run → Watch code/browser sandbox → Inspect 3 findings → Verify $180 price delta → Review recommended draft → Export evidence report.** Include a separate deliberate infinite-loop containment demonstration, never on a real third-party site.

## 8. Success criteria and decision gates

**Minimum submission gate:** mission API + UI works; actual sandbox code execution; Vultr inference is the only model provider; pricing finding correct; an accessible evidence view; a recorded containment test; live Vultr deployment. If time is limited, skip advanced visuals and replay before compromising this chain.

**Stretch gate:** browser verification, export PDF, signed evidence manifest, retry replay, multi-step comparison. If browser path fails, show stable code-only execution and explicitly document Pattern A only.

## 9. Business value hypothesis

Reducing manual exception search could make invoice operations more auditable. The initial synthetic demo **does not prove time savings in real firms**. A future pilot must measure reviewer minutes per 100 invoices, exception precision/recall, rework rate, and approver trust; see [`15-BUSINESS-AND-METRICS.md`](15-BUSINESS-AND-METRICS.md).

## 10. Dependencies and exclusions

Vultr compute availability, Vultr inference subscription/key and supported model, isolated worker support on selected VM, staged demo input, usable public domain/TLS, available event credits and acceptable licensing. Nothing here implies access to Vultr credentials has been provided.
