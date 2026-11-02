# Synthetic Dataset Specification and Ground Truth

## Fixture ID

`demo-2026-11-v1` · Source files: `fixtures/synthetic/invoices.csv`, `fixtures/synthetic/purchase_orders.csv`, `fixtures/synthetic/expected_findings.json`.

## Data contract

**Invoices:** 150 rows, columns `record_id`, `vendor_id`, `supplier_invoice_number`, `po_id`, `sku`, `quantity`, `unit_price_cents`, `currency`. **Purchase orders:** 150 rows, columns `po_id`, `vendor_id`, `sku`, `quantity`, `unit_price_cents`, `currency`. All synthetic; currencies USD; positive integer quantities and prices.

Each valid invoice maps to exactly one PO by `(po_id,sku)`. Duplicate detection uses `(vendor_id,supplier_invoice_number)` across *different* `record_id`s. Invalid PO links are not silently remapped.

## Injected cases / oracle

| Fixture | Defect | Expected result | Monetary semantics |
|---|---|---|---|
| INV-0042 | Invoice price 13800 cents vs approved PO 12000 cents, qty 10 | `PRICE_VARIANCE`, `amount_cents=18000` | $180 price overage |
| INV-0087 | Same vendor and supplier number as INV-0086 | `POSSIBLE_DUPLICATE` pair 86/87 | Do not count as verified $ loss |
| INV-0121 | PO `PO-NOT-FOUND-121` absent from PO file | `UNKNOWN_PO` | Not quantified |

All other 146 invoice records are ordinary; the possible-duplicate finding references two invoices. Output **three exception findings** and **$180 verified pricing variance**, not “$180 total exposed to payment fraud.”

## Fixture generation and determinism

Files are committed as static deterministic fixtures; sample generator is permitted to regenerate them if it produces byte-identical outputs. Use static ISO timestamps or none; avoid current-time fields changing hash. Verify via `python3 scripts/validate_fixtures.py`, which checks row counts, one known price mismatch, one pair duplicate and one missing PO. It is independent of any AI model.

## Synthetic vendor portal

If Pattern B is built, host a project-controlled mock portal with PO and invoice detail pages. The portal must not accept real credentials or expose internet browsing. A deliberately malicious HTML notice may test prompt injection but must never instruct the evaluator to attack a third-party site. The screenshot evidence references controlled origin, timestamp and artifact SHA-256.

## Evaluation protocol

1. Parse and validate both CSVs.
2. Compute canonical source SHA-256 and normalize price/quantity types.
3. Run agent's isolated analysis and collect output.
4. Run trusted fixture oracle, compare finding types, record IDs and amount.
5. Record precision/recall on this **single synthetic fixture only**. This is not a claim about real-world performance.
6. Store failed runs; never silently adjust fixture truth to match wrong model outputs.

## Privacy and legal considerations

Every vendor ID and invoice is artificial. Do not import real accounting exports into public demo. Keep fixture use under MIT license and avoid copying proprietary vendor documents or personal information.
