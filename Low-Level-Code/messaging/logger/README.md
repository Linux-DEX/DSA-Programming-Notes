# Multi-level logger

Levels are `DEBUG`, `INFO`, `WARN`, and `ERROR`. A logger fans a line
out to every handler. Each handler drops lines below its own level.

`ConsoleHandler` writes to a stream. `FileHandler` appends to a path.
The demo points the console handler at a buffer and the file handler
at a temporary file, with the file accepting debug lines the console skips.

## Run

```bash
python main.py
```
