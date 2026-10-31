# Elevator

One car. `request(floor)` adds a stop. `step()` either opens the doors
at the current floor or moves one floor.

The car keeps its direction until there is no requested floor ahead,
then it reverses. That is SCAN for a single car.

## Run

```bash
python main.py
```
