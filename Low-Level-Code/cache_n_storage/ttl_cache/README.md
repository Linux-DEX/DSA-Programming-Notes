# TTL Cache with LRU Eviction

A cache implementation supporting expiration and LRU eviction.

## Features

- Per-entry TTL.
- Default TTL support.
- Automatic expiration checks on get.
- Expired-entry cleanup during put.
- LRU eviction when capacity is reached.
- Manual deletion.

## Data Structures

- `Node`: Stores key, value, expiration timestamp and pointers.
- `HashMap`: Maps keys to cache nodes.
- `DoublyLinkedList`: Maintains LRU ordering.
- `TTLCache`: Handles expiration and eviction.

## Eviction Policy

1. Expired entries are removed first.
2. If capacity is still full, evict the LRU entry.
3. Insert the new entry at the MRU position.

## Complexity

| Operation       | Time Complexity |
| --------------- | --------------- |
| Get             | O(1)            |
| Delete          | O(1)            |
| LRU eviction    | O(1)            |
| Put             | O(n)            |
| Cleanup expired | O(n)            |

## Run

```bash
python main.py
```
