# Circuit breaker

Wrap a call that depends on something else.

- **closed** — the call runs. Failures count toward `failure_threshold`.
- **open** — the call is rejected with `CircuitOpenError` and the function does not run.
- **half-open** — after `reset_timeout`, one call is allowed through. Success closes the breaker. Failure opens it again.

## Run

```bash
python main.py
```
