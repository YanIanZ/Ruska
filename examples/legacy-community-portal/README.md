# Owned Legacy Portal — Black-Box HTTP Fixture

This **project-authored fictional** 2008-style community service portal is the safe target for RUKSA RELIC browser archaeology. Its most interesting conditional validation rule now lives **on the server**, not in the browser script. A browser-only observer must discover it by trying approved synthetic inputs.

## Run locally (Python standard library)
\`\`\`bash
python3 examples/legacy-community-portal/server.py --port 8765
# Open http://127.0.0.1:8765
python3 -m unittest discover -s tests -p "test_relic_*.py" -v
\`\`\`

- GET / serves the intentionally dated form.
- POST /api/request accepts an exact JSON structure and returns accepted/code or rejected/error_code; no data stored.
- GET /healthz reports fixture process health.
- Only loopback binding is supported. No credentials, users, external integrations or production submissions.
- The browser sees the HTTP contract and responses, not the Python source. Source is in GitHub **for transparent evaluation**, but the future agent is meant to use an owner-authorized browser surface rather than repository code.

## Important boundaries
The server HTTP tests are a real local HTTP service, not a Playwright trace or a sandbox on Vultr. The fixture's authored rule and truth set live in Python and synthetic JSON, not real hidden business logic. For challenge compliance, the agent must still run Playwright in a separately isolated Vultr execution worker and use Vultr Serverless Inference.
