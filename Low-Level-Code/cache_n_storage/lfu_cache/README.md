# LFU Cache - Least Frequently Used

## 1. Introduction

LFU (Least Frequently Used) Cache is a caching mechanism
that stores frequently accessed data in memory.

When the cache reaches its maximum capacity, it removes
the entry with the lowest access frequency.

If multiple entries have the same frequency, LRU
(Least Recently Used) is used as a tie-breaking policy.

## 2. Objectives

- Understand caching mechanisms.
- Implement LFU eviction from scratch.
- Understand hash maps and linked lists.
- Understand object references in Python.
- Achieve O(1) average time complexity for GET and PUT.

## 3. Architecture

The implementation uses three primary data structures.

### A. Hash Map

Maps cache keys to their corresponding nodes.

    cache = {
        key: Node
    }

Purpose:

- Fast key lookup.
- Direct node access.

### B. Frequency Map

Maps access frequency to a doubly linked list.

    freq_map = {
        frequency: DoublyLinkedList
    }

Purpose:

- Group entries by access frequency.
- Avoid scanning all cache entries.

### C. Doubly Linked List

Maintains recency order within each frequency bucket.

    HEAD <-> A <-> B <-> TAIL

- Front: Most recently used.
- Back: Least recently used.

## 4. Internal Architecture

LFUCache
|
|-- cache (key -> Node)
|
|-- freq_map (frequency -> LinkedList)
|
|-- min_freq

Each node belongs to exactly one frequency bucket.

## 5. Operations

### GET(key)

1. Find the node in the cache dictionary.
2. Return -1 if missing.
3. Remove the node from its current frequency list.
4. Increase its frequency.
5. Insert it into the next frequency list.
6. Return its value.

### PUT(key, value)

1. Update an existing entry and increase frequency.
2. If capacity is available, insert a new entry.
3. If full, evict the LFU entry.
4. Apply LRU when frequencies are equal.
5. Insert the new entry with frequency 1.

## 6. Complexity

| Operation   | Complexity   |
| ----------- | ------------ |
| GET         | O(1) average |
| PUT         | O(1) average |
| Insert node | O(1)         |
| Remove node | O(1)         |
| Eviction    | O(1)         |

## 7. Future Improvements

- TTL expiration.
- Thread safety.
- Memory-based capacity.
- Cache metrics.
- Persistent storage.
- Benchmarking.
