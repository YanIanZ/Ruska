#!/usr/bin/env python3
"""Project-owned synthetic legacy service.

Local demo ONLY. No auth, persistence or production data. Rules live on the
server so a browser observer must infer them from approved synthetic probes.
"""
from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

PORTAL = Path(__file__).resolve().with_name("index.html")
MAX_BYTES = 4096
REGIONS = {"North", "Center", "South"}
ISSUES = {"streetlight", "drain", "pavement"}
PRIORITIES = {"normal", "urgent"}


def evaluate_request(data: Any) -> tuple[int, dict[str, Any]]:
    """A deliberately undocumented-on-client mock behavioral contract."""
    expected = {"region", "issue", "priority", "description"}
    if not isinstance(data, dict) or set(data) != expected:
        return 422, {"accepted": False, "error_code": "INVALID_FIELDS"}
    if any(type(data[key]) is not str or len(data[key]) > 1000 for key in expected):
        return 422, {"accepted": False, "error_code": "INVALID_FIELDS"}
    region, issue, priority = data["region"], data["issue"], data["priority"]
    description = data["description"].strip()
    if not region:
        return 422, {"accepted": False, "error_code": "REGION_REQUIRED"}
    if region not in REGIONS or issue not in ISSUES or priority not in PRIORITIES:
        return 422, {"accepted": False, "error_code": "INVALID_FIELDS"}
    if priority == "urgent" and len(description) < 30:
        return 422, {"accepted": False, "error_code": "URGENT_DESCRIPTION_TOO_SHORT"}
    return 200, {"accepted": True, "code": f"{region}-{issue}-{priority}".upper()}


class Handler(BaseHTTPRequestHandler):
    server_version = "RELICLegacyFixture/1.0"

    def log_message(self, format_string: str, *args: object) -> None:
        """Avoid logging user-provided synthetic payloads."""
        pass

    def send_payload(self, status: int, data: bytes, media: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", media)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self' 'unsafe-inline'; connect-src 'self'; object-src 'none'")
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, status: int, data: dict[str, Any]) -> None:
        self.send_payload(status, json.dumps(data, separators=(",", ":")).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self) -> None:
        if self.path == "/":
            self.send_payload(200, PORTAL.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/healthz":
            self.send_json(200, {"healthy": True, "fixture": "project-owned"})
        else:
            self.send_json(404, {"error": "NOT_FOUND"})

    def do_POST(self) -> None:
        if self.path != "/api/request":
            self.send_json(404, {"error": "NOT_FOUND"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            size = 0
        if size <= 0 or size > MAX_BYTES:
            self.send_json(413, {"error": "INVALID_BODY_SIZE"})
            return
        if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != "application/json":
            self.send_json(415, {"error": "CONTENT_TYPE"})
            return
        try:
            payload = json.loads(self.rfile.read(size).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_json(400, {"error": "INVALID_JSON"})
            return
        status, result = evaluate_request(payload)
        self.send_json(status, result)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run owned RELIC legacy mock service (no production use)")
    parser.add_argument("--host", default="127.0.0.1", help="Default loopback; do not expose to public Internet")
    parser.add_argument("--port", default=8765, type=int)
    args = parser.parse_args()
    if args.host not in ("127.0.0.1", "localhost", "::1"):
        parser.error("Only loopback host is supported by this synthetic fixture")
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"RELIC synthetic legacy portal on http://{args.host}:{server.server_port} (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
