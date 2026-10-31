# Movie ticket booking

A show owns a set of seats. `book` takes every requested seat or none
of them. The check and the update share one lock, so two threads cannot
sell the same seat.

## Run

```bash
python main.py
```
