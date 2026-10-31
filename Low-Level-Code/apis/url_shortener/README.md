# URL shortener

`shorten(url)` returns a base62 code. The same URL returns the same code.
`resolve(code)` returns the URL, or `None` when the code was never issued.

Codes come from an increasing counter. Both maps are in memory.

## Run

```bash
python main.py
```
