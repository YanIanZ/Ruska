# Deterministic Synthetic Procurement Fixture

Contains 150 fake purchase orders and 150 fake invoice records, with **three seeded exception scenarios**. Data is not taken from any real firm, provider, vendor, payment card or identifiable person.

- `INV-0042` has `quantity=10`, `unit_price_cents=13800`, matching `PO-0042` price `12000`, so price variance is `18000 cents` = **$180**.
- `INV-0087` repeats the supplier invoice number used in `INV-0086` for the same synthetic vendor, yielding one **possible duplicate pair**.
- `INV-0121` references `PO-NOT-FOUND-121`, yielding one **unknown PO**.
- The other 146 records should not yield exception findings.

The expected output is specified in `expected_findings.json`. Do **not** interpret the duplicate or missing PO as confirmed financial loss. Price variance is $180; total risk exposure is deliberately not computed.

Run `python3 scripts/validate_fixtures.py` from repository root to validate fixtures. That script does not prove any AI runtime, sandbox behavior or cloud integration.

For a later browser demo, build a **project-owned** vendor test portal displaying these records. Avoid external live services.
