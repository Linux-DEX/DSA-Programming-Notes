# Bloom filter

A compact set that can say "definitely not here" or "maybe here".

## How it works

Each insert sets `hash_count` bits in a byte array. A lookup checks those
same bits. If any bit is off, the item was never inserted. If all are on,
the item might have been inserted, or other items may have set the same bits.

Items cannot be deleted. Clearing a bit could hide a different item.

## Complexity

| Operation      | Time        |
| -------------- | ----------- |
| add            | O(k)        |
| might_contain  | O(k)        |

`k` is `hash_count`. Space is `size` bytes.

## Run

```bash
python main.py
```
