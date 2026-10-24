from functools import lru_cache
import time

# ---------
# 1. clear on write — mutation of backing data invalidates reads

discounts = {1: 10}   # pretend this is the database

@lru_cache(maxsize=None)
def get_discount(user_id: int) -> int:
    return discounts[user_id]

print(get_discount(1))            # miss → 10
discounts[1] = 50                 # backing value changed
print(get_discount(1))            # still 10 — STALE, cache doesn't know

get_discount.cache_clear()        # explicit invalidation on write
print(get_discount(1))            # fresh → 50

# ---------
# version in the key — a global version bumps keys instead of clearing

DATA_VERSION = 0

def bump_version():
    global DATA_VERSION
    DATA_VERSION += 1

def get_config(key: str) -> str:
    return f"{key}@v{DATA_VERSION}"   # pretend this reads new data

@lru_cache(maxsize=None)
def cached_config(key: str, _version: int) -> str:
    return get_config(key)

def get_config_cached(key: str) -> str:
    # caller always reads via this; keys change when version bumps
    return cached_config(key, DATA_VERSION)

print(get_config_cached("theme"))     # miss → computed
print(get_config_cached("theme"))     # hit → same cached value
bump_version()                        # backing data changed
print(get_config_cached("theme"))     # new key → miss → fresh value
# note: old entries are unreachable now but still occupy the cache
# (maxsize eviction or cache_clear handles that eventually)

# ---------
# time-bucket TTL trick — "expire every 60s" via a rotating key part

BUCKET_SECONDS = 3   # small bucket so the demo finishes quickly

@lru_cache(maxsize=None)
def get_rates(key: str, _bucket: int) -> str:
    return f"rates@{key}/bucket{_bucket}"   # pretend fresh fetch

def get_rates_cached(key: str) -> str:
    bucket = int(time.monotonic() // BUCKET_SECONDS)
    return get_rates(key, bucket)

print(get_rates_cached("EUR"))    # bucket N
print(get_rates_cached("EUR"))    # same bucket → hit
time.sleep(BUCKET_SECONDS)        # wait for bucket rotation
print(get_rates_cached("EUR"))    # new bucket → fresh value

# ---------
# 3. custom TTL decorator — validates expiry before returning (per-key possible)

def ttl_cache(seconds: float):
    def decorator(fn):
        store = {}                       # key -> (expires_at, value)
        def wrapper(*args):
            now = time.monotonic()
            hit = store.get(args)
            if hit and hit[0] > now:
                return hit[1]            # valid hit
            value = fn(*args)            # recompute on miss/expiry
            store[args] = (now + seconds, value)
            return value
        wrapper.clear = store.clear      # full clear (per-key too if we wanted)
        return wrapper
    return decorator

calls = {"n": 0}

@ttl_cache(seconds=1)
def slow_value(x: int) -> int:
    calls["n"] += 1
    return x * 2

print(slow_value(5), slow_value(5))   # 10 10 — computed once
print(calls["n"])                     # 1
print(slow_value(7))                  # 14 — new key → computed
print(calls["n"])                     # 2
time.sleep(1)                         # TTL expires
print(slow_value(5))                  # 10 again but RE-computed
print(calls["n"])                     # 3

# ---------
# 4. file snapshot validation — self-healing cache via mtime

import os
import tempfile

def mtime_cache(fn):
    stat_cache = {}   # path -> (mtime, value)
    def wrapper(path):
        mtime = os.stat(path).st_mtime
        hit = stat_cache.get(path)
        if hit and hit[0] == mtime:
            return hit[1]            # file unchanged → cached
        value = fn(path)             # file changed → recompute
        stat_cache[path] = (mtime, value)
        return value
    return wrapper

@mtime_cache
def read_file(path: str) -> str:
    with open(path) as f:
        return f.read()

path = os.path.join(tempfile.gettempdir(), "lru_note_demo.txt")
with open(path, "w") as f:
    f.write("v1")

print(read_file(path))               # v1
with open(path, "a") as f:           # rewrite the backing file
    f.write("+-v2")

print(read_file(path))               # v1+-v2 — cache noticed mtime change by itself
os.remove(path)                      # cleanup

# ---------
# what maxsize alone does NOT give you — stale until evicted

@lru_cache(maxsize=1)   # tiny cache → values eventually recompute, but unbounded staleness window
def eventually_fresh(x: int) -> int:
    return x

print(eventually_fresh(1), eventually_fresh(2), eventually_fresh(1))
print(eventually_fresh.cache_info())   # note the miss after eviction — "eventually fresh", no guarantee of when
