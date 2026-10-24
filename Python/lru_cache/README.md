# functools — `lru_cache`

- `functools` is a standard library module with higher-order tools that work on functions (decorators like `lru_cache`, `@cache`, `@wraps`, utilities like `reduce`, `partial`).
- `lru_cache` is a **memoization decorator**: it caches the return value of a function, keyed by its arguments.
- LRU = **Least Recently Used**. When the cache is full, the *least recently used* entry is evicted to make room for the new one.
- One decorator line can turn an exponential-time recursive solution into linear time (classic DSA use case: fibonacci, coin change, DP on recursion).

Official docs: [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)

---

## How it works

1. The function is called with some arguments.
2. `lru_cache` computes a hashable key from those arguments and looks it up in the cache.
3. **Hit** → cached result is returned instantly; the entry is moved to the "most recently used" position.
4. **Miss** → the real function runs, its result is stored, and `misses` counter goes up.
5. If the cache has reached `maxsize`, the entry at the LRU end gets evicted.

> [!NOTE]
> Arguments must be **hashable**. Lists, dicts, sets, generators → `TypeError: unhashable type`.

---

## Inside the LRU cache (LeetCode 146 connection)

Internally `lru_cache` is exactly what "Design an LRU Cache" (LeetCode 146) asks you to build from scratch — the stdlib is the reference answer:

- A **hash map/dict** keyed by the normalized argument tuple → O(1) lookup.
- A **doubly-linked list** ordered most-recently-used → last → O(1) move-to-front and O(1) evict-from-back.

Dict alone can't do LRU eviction in O(1); a linked list alone can't find entries in O(1); together both operations are O(1). Any DSA notes on LRU design can point back here as the "production-grade" version, and any `lru_cache` behavior in this README maps onto that linked-list bookkeeping.

The natural follow-up problem is **LeetCode 460 "LFU Cache"** (evict least-*frequently*-used, tie-break by recency) — `lru_cache` does not do this; see the toolbox comparison below.

### Key normalization — why some calls "mysteriously" hit or miss

The cache key is a **normalized tuple of arguments**, built from the call signatures. So positional and keyword styles of the same call share one cache entry:

```python
@lru_cache
def f(a, b): ...

f(1, 2)      # miss
f(1, b=2)    # hit — same normalized key
f(2, 1)      # miss — order matters, keys are NOT set-like for bare values
```

Two consequences to internalize:
- Mixing positional/keyword call styles does **not** fragment the cache.
- Symmetry is *not* assumed by the cache: `f(2, 1)` ≠ `f(1, 2)` — if order shouldn't matter, normalize arguments yourself (e.g. `f(sorted(x))` for multi-arg symmetric problems).

See: [`lru_cache.py`](./lru_cache.py)

---

## Parameters

| Parameter | Default  | Description                                                        |
|-----------|----------|--------------------------------------------------------------------|
| `maxsize` | `128`    | Max number of entries. `None` = unbounded (grows forever). `0` = **never cache** (every call is a miss — handy to A/B benchmark hits vs. no-cache). |
| `typed`   | `False`  | If `True`, treats `1` and `1.0`, `True` and `1` as *different* keys. |

```python
# plain with default maxsize=128
@lru_cache
def f(x): ...

# explicit
@lru_cache(maxsize=None, typed=True)
def g(x): ...

# equivalent style
@lru_cache()
def h(x): ...
```

---

## `cache_info()`

Every decorated function exposes `cache_info()` returning a named tuple:

| Field     | Meaning                                        |
|-----------|------------------------------------------------|
| `hits`    | Times a lookup found a cached value.           |
| `misses`  | Times the function actually ran.               |
| `maxsize` | The configured size.                           |
| `currsize`| Entries currently in the cache.                |

- **`f.cache_clear()`** — wipes the whole cache (useful between tests or fresh runs).
- **`f.__wrapped__`** — escape hatch to call the original, uncached function.
- Use `hits / (hits + misses)` as a rough payoff ratio: if it's low, the cache isn't helping.

---

## Example: Memoization / DSA Angle

Without caching, naive `fib(n)` recomputes the same subproblems over and over → **O(2ⁿ)**.
With `@lru_cache`, each subproblem is computed exactly once → **O(n)** time, **O(n)** space.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

This is the same idea as **top-down dynamic programming** — `lru_cache` is what makes top-down DP trivial in Python.

Two more DP patterns worth having in muscle memory (see [`lru_cache.py`](./lru_cache.py) for runnable versions):

```python
# grid paths — a 2D state (row, col) as the key
@lru_cache(maxsize=None)
def paths(r, c):
    if r == 0 or c == 0:
        return 1
    return paths(r - 1, c) + paths(r, c - 1)

# coin change — state is the remaining amount, "args" stay scalar
@lru_cache(maxsize=None)
def fewest_coins(amount, coins=frozenset({1, 5, 12, 19})):
    if amount == 0:
        return 0
    best = amount + 1
    for coin in coins:
        if coin <= amount:
            best = min(best, 1 + fewest_coins(amount - coin, coins))
    return -1 if best > amount else best
```

Takeaway: whatever the recursion state is, it must be **small, hashable, and complete** — that state tuple becomes the cache key and the DP table index.

See: [`lru_cache.py`](./lru_cache.py)

---

## When to use it / gotchas

- **Good for:** pure functions (same input → same output), expensive computations, recursive DP solutions, repeated config/data lookups.
- **Not ideal for:** functions with side effects (I/O writes, randomness), objects that mutate between calls, values that must stay fresh.
- **Findable via `functools.cache`** — a 3.9+ shorthand for `lru_cache(maxsize=None)`.
- On **methods**, the cache key includes `self`, so instances are kept alive by the cache and their attributes are *not* compared — a mutated attribute won't invalidate the cached value. For methods, think carefully or scope the caching to a helper function. The stdlib's purpose-built fix is **`functools.cached_property`** (see [Caching a method the right way](#caching-a-method-the-right-way--cached_property)).
- **`lru_cache` is not selective about *why* an object is unhashable**: by default it hashes each argument with `hash()`. Watch out for things that *are* hashable but shouldn't be:
  - **numpy arrays** — `hash(np.array([1, 2]))` raises `TypeError` like a list does, so direct caching just fails. Convert the data explicitly first: `arr.tobytes()` (fast, but 5000-element arrays blow the hashing cost up) or `tuple(arr)` — this makes it *your* decision where the key-vs-cost tradeoff sits, instead of a silent failure.
  - **large objects passed by value** (tuples of long strings, big containers that you hash) — every call pays the hashing cost, which can dominate the savings.
- **When the cache is a pessimization**, not an optimization:
  - cheap functions — the wrapper's locking, key hashing, and dict lookups can cost more than the call itself (`hits` go up but wall time got worse).
  - low hit ratio: if every call uses fresh arguments, you pay memory + hash overhead for *nothing*; check `hits / (hits + misses)` before declaring victory.
  - huge return values with high cardinality — each distinct result stays pinned in RAM (worse with `maxsize=None`).
- It is **thread-safe**: gets and puts are locked, so it composes fine with `threading` (see `Multithreading/README.md`), though under heavy contention threads queue on that lock.

---

## Stale Cache / Invalidation Strategies

`lru_cache` keys only on the arguments passed in — it has **no idea** if the value behind that call changed. If the backing data mutates, the stale value keeps being served forever (or until eviction). Invalidation must be added on top. Main strategies, roughly simplest → most robust:

### 1. Clear on write (event-driven invalidation)

Whenever the underlying data is mutated, wipe the cache:

```python
@lru_cache(maxsize=None)
def get_discount(user_id): ...

def set_discount(user_id, value):
    db.save(user_id, value)
    get_discount.cache_clear()      # a write invalidates reads
```

- **Con:** you can't delete a *single* key from `lru_cache` — only `cache_clear()` (everything). Fine for small caches, wasteful if entries are expensive to rebuild.
- `cache_clear()` only prevents *future* staleness; a concurrent reader can still briefly see the old value in flight (thread-safe though).

### 2. Version / timestamp inside the cache key

Don't clear — make the *key itself change* when data changes. New key = miss = fresh value; old entries become unreachable garbage.

```python
DATA_VERSION = 0

def bump_version():
    global DATA_VERSION
    DATA_VERSION += 1

@lru_cache(maxsize=None)
def get_config(key, _version=DATA_VERSION):  # version is part of the key
    return load_from_db(key)
```

Cleaner variant — the **time-bucket TTL trick**, no custom decorator needed:

```python
@lru_cache(maxsize=None)
def get_rates(key, _bucket=int(time.monotonic() // 60)):  # 60s buckets
    return expensive_fetch(key)
```

Every 60s the bucket rotates → keys never repeat → effectively "cache expires every 60s". Crude but effective.

### 3. Custom decorator that validates before returning

Store a small "snapshot" (timestamp, file mtime, object version) alongside the result and re-check it on every call — true correctness-by-validation:

```python
def ttl_cache(seconds):
    def decorator(fn):
        store = {}                    # key -> (expires_at, value)
        def wrapper(*args):
            now = time.monotonic()
            hit = store.get(args)
            if hit and hit[0] > now:
                return hit[1]
            value = fn(*args)         # recompute on miss/expiry
            store[args] = (now + seconds, value)
            return value
        wrapper.clear = store.clear   # per-key delete possible here
        return wrapper
    return decorator
```

For file-based data, snapshot `os.stat(path).st_mtime` and recompute when it changes — the cache *self-heals* the moment the file is rewritten. Don't hand-roll this in real code: [`cachetools`](https://cachetools.readthedocs.io/) gives `TTLCache`, `LFUCache`, etc. ready-made.

### 4. Bounded `maxsize` as a damper (least robust)

A small `maxsize` means entries get evicted and recomputed regularly — "eventually fresh", with no guarantee of *when*. Use only for data where being briefly stale doesn't matter.

### 5. Key on the real dependencies (fresh-by-identity)

For functions taking objects that mutate, include the mutable state in the key so changes naturally produce misses:

```python
@lru_cache
def total(inventory_row, updated_at):   # updated_at is part of the key
    ...
```

Trades memory for correctness; works only when the dependency is hashable/compact.

### Picking a strategy

<details>
<summary>Cheat table</summary>

| Situation | Typical strategy |
|---|---|
| In-process config/setters you control | 1 — clear on write |
| TTL wanted (API responses, "re-fetch every N min") | 2 (time bucket) or 3 (TTL decorator) |
| Expensive single-user data, reads ≫ writes | 2 — version bump |
| File / DB tables behind the function | 3 — snapshot validation (mtime, `updated_at` column) |
| Per-key invalidation needed | custom dict decorator or `cachetools`/`Redis` — not `lru_cache` |

</details>

> [!IMPORTANT]
> **Rule of thumb:** `lru_cache` is honest for *pure* functions only — same input → same output, forever. The moment the backing value can change, you've left the pure-function world, and one of these strategies moves you to *invalidate on change*, *expire by time*, or *validate dependencies*.

See: [`invalidation.py`](./invalidation.py)

---

## Caching a method the right way — `cached_property`

`lru_cache` on an instance method has the `self` string attached: keys include `self` (via hashing), so instances pin themselves in memory through the cache, and the cache is shared across all instances of the class. **`functools.cached_property`** is the stdlib answer:

```python
from functools import cached_property

class Dataset:
    def __init__(self, path):
        self.path = path

    @cached_property
    def rows(self):            # computed once per instance, stored on the instance itself
        return load_and_parse(self.path)
```

- The computed value is stored **on the instance** (`self.__dict__["rows"]`), not in a global cache → no shared cache, no `self` leaking into a shared key space.
- No `maxsize` — it's per-instance by definition; memory dies with the object instead of the function.
- Writes to the attribute name *replace* the cached value; `del self.rows` recomputes it next access.
- Works with the **ghost/internals of `__get__`** (it's a descriptor), which is also why it only works on classes — not on plain functions.

| Problem | `@lru_cache` on method | `@cached_property` |
|---|---|---|
| Storage | global, keyed by `(self, args...)` | on the instance itself |
| Instance lifetime | instance pinned by cache | dies with the instance |
| Stale attributes | mutated attrs invisible | same — it's still snapshot caching |
| Shared across instances | yes (one cache) | no (each instance independent) |

> [!NOTE]
> `cached_property` requires its class to have a **`__dict__`** — it won't work on classes using `__slots__` without a fallback. Also requires Python 3.8+.

---

## The caching toolbox — one table to rule them all

| Tool | What it caches | Scope / eviction | Use it for |
|---|---|---|---|
| `functools.lru_cache` | function returns, keyed on args | shared global cache, LRU with `maxsize` | pure expensive functions, DP/memoization |
| `functools.cache` | same as `lru_cache(maxsize=None)` | global, unbounded, slightly faster get/put path than lru | recursive DP where the state set is small and known |
| `functools.cached_property` | one computed attribute | per-instance, in `self.__dict__` | expensive one-time derived values on objects |
| custom dict decorator | anything you choose (incl. TTL, per-key delete) | whatever you build | TTL / invalidation needs (see invalidation section) |
| [`cachetools`](https://cachetools.readthedocs.io/) | same shapes + `TTLCache`, `LFUCache` | TTL / LFU / ARC policies | anything needing a real expiry or LFU policy |
| `diskcache` / Redis | persistent, cross-process | LRU/TTL on disk or a server | caches that must outlive the process |

**Rule of escalation:** start with plain `lru_cache`; reach for `cached_property` when the value belongs to an *object*, a custom/TTL decorator when keys must expire individually, and Redis/disk only when the cache must cross process boundaries or survive restarts.

### Cross-links for DSA practice

- **LeetCode 146 — Design LRU Cache**: implement the dict + doubly-linked-list combo by hand; our ["Inside the LRU cache" section](#inside-the-lru-cache-leetcode-146-connection) describes the structure it mirrors.
- **LeetCode 460 — Design LFU Cache**: frequency-based eviction that `lru_cache` deliberately does not do — after 146, build it with a dict of frequency-buckets.
- **Top-down DP with `@cache`**: coin change (LC 322), grid paths (LC 62) — the memoization examples above map one-to-one onto these.
