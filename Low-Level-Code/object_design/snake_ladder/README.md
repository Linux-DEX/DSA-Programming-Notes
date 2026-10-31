# Snake and ladder

Players start at 0, off the board. A roll that would pass the last
square is ignored, so the finish needs an exact roll. A snake or a
ladder moves the player once; the landing square is not checked again.

`play(roll, max_turns)` asks `roll()` for each turn. Pass a function
that returns the next face so a game can be replayed with a fixed dice.

## Run

```bash
python main.py
```
