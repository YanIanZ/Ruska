# Security Policy

**Status:** Design-stage prototype. **Not safe for real financial data or unrestricted third-party code execution.** Security-sensitive behavior is specified in [`docs/06-SECURITY-THREAT-MODEL.md`](docs/06-SECURITY-THREAT-MODEL.md).

Please **do not** test RUKSA against arbitrary third-party sites or upload real confidential data. Report potential issues privately to the repository owner through an available private GitHub contact or GitHub Security Advisories (if enabled). Do not publish secrets or exploit artifacts in public issues.

The team should promptly triage reproducible findings and pause public sandbox execution if isolation or credential handling is compromised. No formal SLA is promised.

Never represent rootless containers as a proof of perfect isolation. All model-generated code must execute in constrained isolated sandboxes, not inside the API runtime. Real customer-facing use requires a new security assessment.
