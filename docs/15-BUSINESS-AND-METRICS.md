# Business Case, Metrics and Commercial Hypotheses

## Target buyer

Mid-market procurement operations, controllers, managed accounting teams and procurement BPOs that handle repeatable supplier invoice/PO comparisons. Their cost is review time plus exception triage, not generative AI inference alone.

## Value proposition

- **Speed:** process repeated invoice-to-PO comparisons; humans review exceptions rather than every line.
- **Trust:** verified findings link to immutable input snapshots and deterministic checks.
- **Control:** approval before downstream actions and restricted sandbox execution.
- **Portability:** structured outputs enable future ERP adapters rather than custom prompts per workflow.

## Evidence of business value required

Do not claim quantified savings from the synthetic benchmark. Future 2–4 week pilot: measure *time to review 100 invoices*, *false positive rate*, *missed exception rate*, *time to resolve anomaly*, *manual correction rate*, *cost per mission*, and *operator perceived clarity* across at least two data patterns.

### Example measurement formulas

- Precision = true positive exceptions / all flagged exceptions.
- Recall = true positive exceptions / all ground-truth exceptions.
- Time saved = baseline manual handling minutes − human review and exception handling minutes.
- Cost per mission = Vultr inference cost + compute allocated cost + storage/egress + operations estimate.
- Evidence coverage = verified findings with all required evidence artifacts / all verified findings. Target **100% by definition** (status cannot be `VERIFIED` otherwise).

For 150-fixture benchmark the expected target is 3 planted exceptions and $180 *verified price variance*. No empirical time-savings or fraud prevention claims are justified by this fixture.

## Product packaging hypothesis

1. **Developer sandbox demo:** free test fixture missions, quotas, public read-only sample outputs.
2. **Ops Team:** usage-priced monthly reconciliation runs, export and approval traceability.
3. **Enterprise:** private deployment, custom retention, SSO/RBAC, ERP adapters and review policies.

Pricing is research hypothesis only. Do not publish unvalidated rates, false SOC 2 claims, or claim certification.

## Expansion roadmap

Start narrow: invoice/PO reconciliation with verified evidence. Then targeted vendor communications, purchase-order change history, three-way match, duplicate-payment risk analysis, and constrained connectors. Later extend EVP-1 to other workflows (support triage, compliance checks, financial close); every domain must define deterministic verification rules and threat boundaries.

## Go-to-market validation

Interview 5–10 real finance/procurement analysts with a demo that uses only synthetic examples. Ask for documented review procedures, typical invoice volume, data systems, acceptable false positives and audit evidence requirements. Do not solicit or store real customer invoices in hackathon public demo.
