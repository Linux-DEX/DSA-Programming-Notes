# Delayed job queue

`schedule(run_at, job)` stores a job on a heap keyed by a monotonic
timestamp. `get()` waits until the earliest job is due, then returns it.
`close()` unblocks a waiter when the heap is empty.

## Run

```bash
python main.py
```
