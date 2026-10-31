# In-memory key-value store

A process-local map with get, set, delete, and per-key TTL.

## Behavior

- `set(key, value, ttl)` stores a value. Pass `ttl=None` when the key should not expire.
- `get` returns the value, or `None` when the key is missing or expired.
- `delete` returns `True` when a live key was removed.
- `ttl` returns seconds remaining, `-1` when the key does not expire, and `-2` when it is missing.
- Expiry is checked on read. There is no background thread.

## Complexity

| Operation | Time |
| --------- | ---- |
| get       | O(1) |
| set       | O(1) |
| delete    | O(1) |
| ttl       | O(1) |

## Run

```bash
python main.py
```
