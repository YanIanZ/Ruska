#!/usr/bin/env python3
"""Deterministically generate synthetic procurement data. Not a production application."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "fixtures" / "synthetic"
OUT.mkdir(parents=True, exist_ok=True)

po_fields = ["po_id", "vendor_id", "sku", "quantity", "unit_price_cents", "currency"]
invoice_fields = ["record_id", "vendor_id", "supplier_invoice_number", "po_id", "sku", "quantity", "unit_price_cents", "currency"]
pos, invoices = [], []
for n in range(1, 151):
    ident = f"{n:04d}"
    vendor = "VENDOR-02" if n in (86, 87) else f"VENDOR-{n % 5:02d}"
    sku = f"SKU-{ident}"
    qty = 10 if n == 42 else 3 + n % 6
    po_price = 12000 if n == 42 else 2500 + (n % 9) * 500
    po = {"po_id": f"PO-{ident}", "vendor_id": vendor, "sku": sku, "quantity": qty,
          "unit_price_cents": po_price, "currency": "USD"}
    invoice = {"record_id": f"INV-{ident}", "vendor_id": vendor,
               "supplier_invoice_number": "SUP-0086" if n == 87 else f"SUP-{ident}",
               "po_id": "PO-NOT-FOUND-121" if n == 121 else po["po_id"],
               "sku": sku, "quantity": qty,
               "unit_price_cents": 13800 if n == 42 else po_price, "currency": "USD"}
    pos.append(po)
    invoices.append(invoice)

for filename, fields, rows in (("purchase_orders.csv", po_fields, pos),
                               ("invoices.csv", invoice_fields, invoices)):
    with (OUT / filename).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

oracle = {
    "dataset_id": "demo-2026-11-v1",
    "record_count": 150,
    "purchase_order_count": 150,
    "expected_exception_count": 3,
    "verified_price_variance_cents": 18000,
    "currency": "USD",
    "cases": [
        {"type": "PRICE_VARIANCE", "invoice_record_ids": ["INV-0042"],
         "po_id": "PO-0042", "amount_cents": 18000,
         "rule_id": "price_variance_v1"},
        {"type": "POSSIBLE_DUPLICATE", "invoice_record_ids": ["INV-0086", "INV-0087"],
         "amount_cents": None, "rule_id": "duplicate_supplier_number_v1"},
        {"type": "UNKNOWN_PO", "invoice_record_ids": ["INV-0121"],
         "po_id": "PO-NOT-FOUND-121", "amount_cents": None,
         "rule_id": "missing_po_reference_v1"}
    ],
    "note": "Synthetic ground truth only. No observed financial impact, bank transactions or real invoices."
}
(OUT / "expected_findings.json").write_text(json.dumps(oracle, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {len(invoices)} invoices, {len(pos)} purchase orders and fixture oracle")
