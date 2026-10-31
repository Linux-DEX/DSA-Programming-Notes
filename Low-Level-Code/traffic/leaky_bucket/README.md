# Leaky bucket

A request adds water. Water leaks at a fixed rate. If the next request
would rise above `capacity`, it is rejected and the level stays put.

The token bucket in `rate_limiter/token_bucket.py` refills tokens.
This one drains water. Both cap the burst, then the steady rate.

## Run

```bash
python main.py
```
