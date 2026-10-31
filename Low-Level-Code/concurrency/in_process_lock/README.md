# In-process distributed lock

One process, many threads, with the rules of a distributed lock:

- `acquire(name, owner, ttl)` returns a fencing token, or `None` if someone else holds a live lease.
- `release` and `renew` require the same owner and token.
- A lease that has expired can be taken by another owner.
- Re-acquiring issues a new token. The old token cannot unlock.

The table is in memory. Other processes cannot see it.

## Run

```bash
python main.py
```
