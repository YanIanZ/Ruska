# Test and Acceptance Plan

## Offline reference suite (implemented)
- 20 unique interleavings of two three-step actors, preserving their own step order.
- Naive policy violates stock conservation in 18 interleavings.
- Atomic policy has 0 violations in the same 20 interleavings.
- Serial schedule may remain safe under naive policy.
- Invalid schedule, unknown policy and unknown fixture fields rejected.
- Report flags all Vultr/LLM/containment status false.

CI: `python3 -m unittest discover -s tests -v`. These are synthetic state-machine tests, not cloud security tests.

## Live implementation acceptance (NOT RUN)
- M1: Vultr inference returns a typed planner output with real model identifier.
- M2: Model-authored executable agent/test code runs only on disposable worker VM guest.
- M3: Trace transported from worker contains run ID, source SHA, actual agent events, exit status and cleanup.
- M4: Go control-plane independent checker rejects falsified state transition/log.
- M5: True baseline violation is replayable from actual event order, after patch same bounded case has no violation.
- M6: Harmless infinite loop terminated within actual wall budget; no leaked worker guest after cleanup.
- M7: Forbidden network/metadata destination access denied; no control-plane keys in guest.
- M8: Public URL with live SSE/events, session authorization and CSRF protection.
- M9: Recorded three-minute demo includes genuine containment.
- M10: Exported result has exact tested coverage and limitations.

## Go/no-go
Any critical safety gate failure disables public arbitrary/generated code execution. If no real worker/inference, application remains a research prototype and submission must be candid.
