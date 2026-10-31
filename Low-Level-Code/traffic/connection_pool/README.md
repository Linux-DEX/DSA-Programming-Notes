# Connection pool

A fixed number of connection objects. `acquire(timeout)` waits until
one is free or raises `TimeoutError`. `release` puts it back.
`execute` on the connection is a stand-in so the example can show reuse
without a real database.

## Run

```bash
python main.py
```
