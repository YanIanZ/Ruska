#!/usr/bin/env python3
"""Independent deterministic fixture consistency checker. Does NOT test live RUKSA service."""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "fixtures" / "synthetic"


def csv_rows(filename):
    with (D / filename).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check():
    po_rows = csv_rows("purchase_orders.csv")
    inv_rows = csv_rows("invoices.csv")
    expected = json.loads((D / "expected_findings.json").read_text(encoding="utf-8"))
    assert len(inv_rows) == expected["record_count"] == 150, "Invoice count mismatch"
    assert len(po_rows) == expected["purchase_order_count"] == 150, "PO count mismatch"
    assert len({p["po_id"] for p in po_rows}) == len(po_rows), "Duplicate PO ID"
    assert len({i["record_id"] for i in inv_rows}) == len(inv_rows), "Duplicate record ID"

    po_by_key = {(p["po_id"], p["sku"]): p for p in po_rows}
    supplier_seen = defaultdict(list)
    for i in inv_rows:
        assert i["currency"] == "USD", "Fixture currency mismatch"
        assert int(i["quantity"]) > 0 and int(i["unit_price_cents"]) > 0, "Invalid quantity/price"
        supplier_seen[(i["vendor_id"], i["supplier_invoice_number"])].append(i["record_id"])

    findings = []
    for (vendor, num), ids in supplier_seen.items():
        if len(ids) > 1:
            findings.append(("POSSIBLE_DUPLICATE", tuple(sorted(ids)), None))

    for i in inv_rows:
        po = po_by_key.get((i["po_id"], i["sku"]))
        if not po or po["vendor_id"] != i["vendor_id"]:
            findings.append(("UNKNOWN_PO", (i["record_id"],), None))
            continue
        # Use integer cents only; no floating-point calculations.
        delta = (int(i["unit_price_cents"]) - int(po["unit_price_cents"])) * int(i["quantity"])
        if delta > 0:
            findings.append(("PRICE_VARIANCE", (i["record_id"],), delta))

    actual = sorted(findings)
    truth = sorted((case["type"], tuple(sorted(case["invoice_record_ids"])), case["amount_cents"])
                   for case in expected["cases"])
    assert actual == truth, f"Fixture exception mismatch: actual={actual} expected={truth}"
    cents = sum(amount for kind, _, amount in actual if kind == "PRICE_VARIANCE")
    assert cents == expected["verified_price_variance_cents"] == 18000, "Price variance mismatch"
    assert len(actual) == expected["expected_exception_count"] == 3, "Exception count mismatch"
    print("PASS: 150 invoices, 150 POs, 3 seeded exceptions, verified $180 price variance (fixture only)")


if __name__ == "__main__":
    try:
        check()
    except (OSError, AssertionError, KeyError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
