# Consistent hashing ring

Keys and nodes sit on a circle. A key belongs to the first node clockwise
from its hash. Removing a node moves only the keys that pointed at it.

Virtual nodes (several points per physical node) keep the split from
depending on one lucky hash.

## API

- `add_node(node)` places `virtual_nodes` points on the ring.
- `remove_node(node)` drops that node's points.
- `get_node(key)` returns the owning node, or `None` when the ring is empty.

## Complexity

| Operation   | Time                          |
| ----------- | ----------------------------- |
| get_node    | O(log R)                      |
| add_node    | O(V log R)                    |
| remove_node | O(V log R)                    |

`V` is virtual nodes per machine. `R` is points currently on the ring.

## Run

```bash
python main.py
```
