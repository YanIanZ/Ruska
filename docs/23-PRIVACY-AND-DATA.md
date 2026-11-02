# SUPERSEDED — Historical RUKSA Concept (NOT CURRENT SCOPE)

> Current product is **RUKSA RELIC**, the Autonomous Digital Restoration Studio. See [active PRD](32-RELIC-PRD.md), [architecture](33-RELIC-ARCHITECTURE.md), and [security](36-RELIC-SECURITY.md). The text below is retained for historical reference and must not be used as RELIC implementation instructions.

---

# Privacy, Data Governance and Responsible Use

## MVP data posture

RUKSA 1.0 is built around **synthetic financial data**. The public demo must not request or process real invoice/customer/employee documents. There is no claim of healthcare, banking or regulatory compliance. The project is a prototype with bounded access and explicit limitations.

## Data classification

| Category | Example | Handling |
|---|---|---|
| Public code/docs | README, diagram, tool schemas | MIT repo; inspect for secrets |
| Synthetic demo data | mock invoices/POs, fake vendor HTML | Can be committed and shown in video |
| Sensitive operational metadata | worker network addresses, sandbox IDs, exact resource host config | Restricted logs, redact public UI as needed |
| Secret | Vultr inference API key, private signer, DB password | VM secret configuration only; never agent-visible |
| Potential private customer content (future) | real invoice, vendor contact, price contract | Out of scope for hackathon demo until consent/legal review |

## Collection and minimization

Collect only fields required for mission and verification. Keep inference contexts sanitized, logs truncated and screenshots limited to approved mock portal. Do not run uncontrolled browser scraping. Demo cookies/sessions should expire and not be used for tracking beyond abuse prevention.

## Retention targets (proposals)

Raw mission uploads/artifacts: 7-day TTL in demo; aggregate run status/metrics: up to 30 days for prototype troubleshooting. Implement and test deletion before publicly claiming these limits. Users should be informed when deletion is enabled. Public source code and static fixture data persist in repo intentionally.

## User rights and transparency

UI clearly marks synthetic environment, stored artifacts, model-generated explanations vs independently verified calculations, and boundaries of human approval. Provide a visible operator disclaimer: *do not upload confidential or regulated data*. If a real-data pilot is pursued, complete consent, retention, security, processor contracts and applicable Indonesian/international legal analysis first.

## Responsible AI policy

No automatic fraud accusation, blacklisting, vendor contact or payment. “Possible duplicate” remains a suspect condition pending review; “Unknown PO” is not proof of misconduct. Explanations cite source data; missing evidence produces an inconclusive outcome. Prompt injection content from CSV/HTML cannot expand agent privileges.

## Public incident response

If someone uploads real sensitive data against instructions, disable affected mission, limit access, delete artifacts where possible, investigate logs for copies, rotate leaked keys and document response. Do not publish sensitive artifacts or screenshots to prove an incident.
