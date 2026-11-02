# Release Checklist — RUKSA 1.0

**Status:** NOT RELEASED. Tick items only after owner has observed evidence from the current candidate commit.

## Identity and compliance

- [ ] RUKSA code license MIT and third-party dependencies reviewed for compatibility.
- [ ] Original work attribution and authorship correct; no prohibited pre-event code if rules restrict it.
- [ ] Official event registration and challenge selection confirmed.
- [ ] Public GitHub repository accessible to a logged-out visitor.
- [ ] README explains Vultr VM, inference, sandbox, and containment honestly.

## Functional P0

- [ ] Real task planning via Vultr Serverless Inference confirmed by observed request/model.
- [ ] Plan validation and policy check before every dispatch.
- [ ] Python code actually executes in disposable sandbox outside app process.
- [ ] 150-row fixture produces three ground-truth anomalies and exactly $180 price variance.
- [ ] Every verified finding links to source data and independent verifier output.
- [ ] User can create mission, see progress, inspect evidence and review draft action.
- [ ] No automated vendor email, payment or ERP update occurs.

## Security and reliability

- [ ] No inference/DB/Vultr/signing secrets present in worker runtime.
- [ ] Timeout and memory limit enforce configured bounds.
- [ ] Sandbox network, filesystem and process isolation tested.
- [ ] Cleanup confirmed for success, failure and timeout.
- [ ] Prompt injection in synthetic document rejected as instructions.
- [ ] Cross-session data isolation, CORS/CSRF policy and session quota verified.
- [ ] Evidence integrity tampering test rejects modified artifact.
- [ ] Repeated job request cannot duplicate run or external effects.
- [ ] Readiness/health endpoints monitored; live public URL tested from clean client.

## Submission

- [ ] Record video (including actual containment and proof output) and check its accessibility.
- [ ] Slide deck and cover image prepared and readable.
- [ ] Repository URL and demo URL copied exactly into lablab form.
- [ ] Description and tech tags match deployed features.
- [ ] Submit before 2026-11-08 22:00 UTC (2026-11-09 05:00 WIB).
- [ ] Capture final lablab submission confirmation and UTC timestamp.

## Signoff record

| Item | Evidence / link | Reviewer | Date |
|---|---|---|---|
| Functional | _pending_ | _pending_ | _pending_ |
| Security | _pending_ | _pending_ | _pending_ |
| Deployment | _pending_ | _pending_ | _pending_ |
| Submission | _pending_ | _pending_ | _pending_ |

**Release principle:** no green checkmarks without real implementation/test evidence. If P0 safety fails, stop rather than fake a successful deployment.
