from functools import lru_cache, cache
import time

# ---------
# basic lru_cache — expensive function, called twice, second call is instant


@lru_cache(maxsize=128)
def expensive_square(n: int) -> int:
    time.sleep(0.5)  # pretend this costs a lot
    return n * n


start = time.perf_counter()
expensive_square(10)  # miss → runs, takes ~0.5s
expensive_square(10)  # hit  → returns instantly from cache
print(f"elapsed with cache: {time.perf_counter() - start:.2f}s")

print(expensive_square.cache_info())
# CacheInfo(hits=1, misses=1, maxsize=128, currsize=1)

# ---------
# maxsize / eviction — LRU keeps the most recent entries


@lru_cache(maxsize=2)
def last_two(n: int) -> int:
    return n


last_two(1)  # cache: [1]
last_two(2)  # cache: [1, 2] (full)
last_two(3)  # evicts 1 (least recently used) → cache: [2, 3]
last_two(1)  # miss again → 1 runs for real
print(last_two.cache_info())  # CacheInfo(hits=0, misses=4, maxsize=2, currsize=2)


# maxsize=None → unbounded cache
@lru_cache(maxsize=None)
def unbounded(n: int) -> int:
    return n


# shorthand since 3.9: functools.cache == lru_cache(maxsize=None)
@cache
def unbounded_shorthand(n: int) -> int:
    return n


# ---------
# typed — True means 1, 1.0, True are distinct cache keys


@lru_cache(maxsize=None, typed=True)
def typed_add(a: int, b: int) -> int:
    return a + b


typed_add(1, 2)
typed_add(1.0, 2)  # separate miss because typed=True
print(typed_add.cache_info())  # misses=2 (would be misses=1 with typed=False)

# ---------
# memoization / top-down DP — fibonacci


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


start = time.perf_counter()
print(f"fib(80) = {fib(80)}")  # instant with cache; naive version would take years
print(f"fib(80) elapsed: {time.perf_counter() - start:.5f}s")
print(fib.cache_info())  # misses=81 → each subproblem computed once

# ---------
# gotcha — arguments must be hashable


@lru_cache
def area(points: tuple) -> int:
    return len(points)


print(area((1, 2)))  # tuple is fine (hashable)
# area([1, 2])                 # TypeError: unhashable type: 'list'

# ---------
# cache_clear() and __wrapped__

fib.cache_clear()  # drop the whole cache
print(fib.cache_info())  # currsize=0 again

# call the original, uncached function (bypasses the cache entirely)
print(fib.__wrapped__(5))

# ---------
# key normalization — f(1, 2) and f(1, b=2) share ONE cache key

@lru_cache
def norm_demo(a, b):
    return (a, b)

print(norm_demo(1, 2))       # miss
print(norm_demo(1, b=2))     # hit — same normalized key
print(norm_demo(2, 1))       # miss — argument ORDER matters, keys are not set-like
print(norm_demo.cache_info())

# ---------
# maxsize=0 — never cache; every call is a miss (great for benchmarking)

@lru_cache(maxsize=0)
def never_cached(x: int) -> int:
    return x * x

never_cached(1)
never_cached(1)
print(never_cached.cache_info())   # hits=0, misses=2 — the decorator still tracks stats

# ---------
# caching can HURT — cheap function, big hashing overhead, low hit ratio

@lru_cache
def cheap(x: int) -> int:
    return x + 1

@lru_cache(maxsize=None)
def cheap_cached(big_key, x: int) -> int:
    return x + 1

big_key = tuple(range(100_000))     # hashing THIS is more expensive than x + 1

start = time.perf_counter()
for _ in range(10_000):
    cheap(1)
print(f"plain cheap fn:        {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
for _ in range(10_000):
    cheap_cached(big_key, 1)        # hits, but each still re-hashes big_key
print(f"cached (big hash key): {time.perf_counter() - start:.4f}s — wrapper overhead can dominate")

# ---------
# numpy arrays are unhashable too — convert explicitly (.tobytes() / tuple)

import numpy as np

@lru_cache
def array_mean(arr_bytes: bytes, shape: tuple) -> float:
    arr = np.frombuffer(arr_bytes, dtype=np.float64).reshape(shape)
    return float(arr.mean())

arr = np.array([1.0, 2.0, 3.0])
print(array_mean(arr.tobytes(), arr.shape))    # key on bytes + shape (hashable)
arr2 = np.array([1.0, 2.0, 3.0])
print(array_mean(arr2.tobytes(), arr2.shape))  # hit — equal contents → equal bytes → same key
print(array_mean.cache_info())

# ---------
# cached_property — caching WITHOUT the method/self leak

from functools import cached_property

class Dataset:
    def __init__(self, rows: int):
        self.rows_count = rows

    @cached_property
    def rows(self):                     # computed once per instance, stored ON THE INSTANCE
        print("computing rows...")
        return list(range(self.rows_count))

ds1 = Dataset(3)
print(ds1.rows)      # prints "computing rows..." then [0, 1, 2]
print(ds1.rows)      # silent hit — no recompute
ds2 = Dataset(5)
print(ds2.rows)      # separate instance → separate computation, nothing shared
del ds1.rows         # drop this instance's cached value → recomputed on next access
print(ds1.rows)      # prints "computing rows..." again

# ---------
# more DSA memoization patterns — 2D states and set-like state in the key

@lru_cache(maxsize=None)
def paths(r: int, c: int) -> int:
    if r == 0 or c == 0:
        return 1
    return paths(r - 1, c) + paths(r, c - 1)

print(f"grid paths(4, 4) = {paths(4, 4)}")      # 70
print(f"grid paths(10, 10) = {paths(10, 10)}")  # 184756

@lru_cache(maxsize=None)
def fewest_coins(amount: int, coins: frozenset) -> int:
    if amount == 0:
        return 0
    best = amount + 1
    for coin in coins:
        if coin <= amount:
            best = min(best, 1 + fewest_coins(amount - coin, coins))
    return -1 if best > amount else best

print(f"fewest_coins(11) = {fewest_coins(11, frozenset({1, 5, 12, 19}))}")   # 3 (5+5+1)
print(f"fewest_coins(2)  = {fewest_coins(2, frozenset({3, 7}))}")            # -1 (impossible)
print(fewest_coins.cache_info())
