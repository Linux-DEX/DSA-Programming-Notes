# Autocomplete

A trie. Each finished word stores how often it was inserted.
`suggest(prefix, k)` walks every word under that prefix and returns
the `k` with the highest frequency. Ties break by the word itself.

## Run

```bash
python main.py
```
