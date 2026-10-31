# Retry with exponential backoff and jitter

`retry(func, attempts, base_delay, max_delay)` calls `func` until it
returns. After a failure it sleeps a random time in
`[0, min(max_delay, base_delay * 2^attempt)]` (full jitter), then tries
again. The last exception is raised when the attempts are used up.

## Run

```bash
python main.py
```
