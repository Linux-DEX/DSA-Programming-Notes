# Read-write lock

Several readers can hold the lock together. A writer waits until every
reader has left, and it holds the lock alone.

A writer that is already waiting blocks new readers, so a stream of
reads cannot keep the writer out forever.

## Run

```bash
python main.py
```
