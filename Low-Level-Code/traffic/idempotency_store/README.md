# Idempotency store

`execute(key, func)` runs `func` once per key.

- A finished key returns the stored result and does not call `func` again.
- A key that is still running raises `RuntimeError`.
- A `func` that raises clears the key so a later call can try again.

The map is in this process. Restarting forgets every key.

## Run

```bash
python main.py
```
