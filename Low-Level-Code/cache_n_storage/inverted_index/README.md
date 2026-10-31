# Inverted index

A search index from token to the documents that contain it.

## Behavior

- Text is lowercased and split into `[a-z0-9]+` tokens.
- `add` replaces a document already stored under the same id.
- `search` is an AND query: every token must appear in the document.
- An empty query returns no documents.

## Complexity

| Operation | Time                                      |
| --------- | ----------------------------------------- |
| add       | O(tokens in the document)                 |
| search    | O(tokens × cost of set intersection)      |

## Run

```bash
python main.py
```
