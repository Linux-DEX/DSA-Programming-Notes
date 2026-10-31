# Bounded blocking queue

FIFO queue with a fixed capacity.

- `put` waits while the queue is full.
- `get` waits while the queue is empty.

Producers and consumers share one condition variable.

## Run

```bash
python main.py
```
