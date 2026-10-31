# Thread pool

`ThreadPool(worker_count)` starts that many workers. `submit(func, args)`
queues a call. `shutdown` finishes queued work, then joins the workers.
A task that raises is printed and the worker keeps taking jobs.

## Run

```bash
python main.py
```
