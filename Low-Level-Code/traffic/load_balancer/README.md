# Load balancer

Three ways to pick a server:

- `round_robin` walks the server list.
- `weighted` walks a list where each server appears `weight` times.
- `least_connections` picks the smallest live count. Ties break by name.

`acquire` increments that count. `release` decrements it.

## Run

```bash
python main.py
```
