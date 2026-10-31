# Parking lot

Spots are `bike`, `compact`, or `large`.

- A bike takes the first free bike spot, then compact, then large.
- A car takes compact, then large.
- A truck takes large.

`park` returns a ticket, or `None` when nothing fits.
`leave(ticket_id)` frees that spot.

## Run

```bash
python main.py
```
