# LRU Cache

An LRU (Least Recently Used) cache implementation using
a Hash Map and Doubly Linked List.

## Data Structures

- `Node`: Stores cache key, value, and linked-list pointers.
- `HashMap`: Maps keys to cache nodes.
- `DoublyLinkedList`: Maintains the order of recently used entries.
- `LRUCache`: Implements cache operations and eviction.

## Eviction Policy

1. Every new entry is inserted at the front.
2. Every accessed entry moves to the front.
3. The back entry is the least recently used.
4. When capacity is reached, remove the back entry.

## Complexity

| Operation     | Average Time |
| ------------- | ------------ |
| Get           | O(1)         |
| Put           | O(1)         |
| Eviction      | O(1)         |
| Move to front | O(1)         |

## Run

```bash
python main.py
```
