# Low-level code

Small Python implementations of the usual low-level interview designs.
Each folder has the code, a `main.py` you can run, and a short README.

LFU, LRU, and the TTL cache were already here. The token bucket, fixed
window, and sliding window rate limiters live in `rate_limiter/`.

## Caches and storage

| Topic | Path |
| ----- | ---- |
| LFU cache | `cache_n_storage/lfu_cache` |
| LRU cache | `cache_n_storage/lru_cache` |
| Cache with TTL and LRU eviction | `cache_n_storage/ttl_cache` |
| In-memory key-value store | `cache_n_storage/kv_store` |
| Bloom filter | `cache_n_storage/bloom_filter` |
| Consistent hashing ring | `cache_n_storage/consistent_hash` |
| Inverted index | `cache_n_storage/inverted_index` |

## Traffic and reliability

| Topic | Path |
| ----- | ---- |
| Token bucket, fixed window, sliding window | `rate_limiter` |
| Leaky bucket | `traffic/leaky_bucket` |
| Circuit breaker | `traffic/circuit_breaker` |
| Retry with exponential backoff and jitter | `traffic/retry_backoff` |
| Load balancer | `traffic/load_balancer` |
| Connection pool | `traffic/connection_pool` |
| Idempotency store | `traffic/idempotency_store` |

## Concurrency

| Topic | Path |
| ----- | ---- |
| Bounded blocking queue | `concurrency/bounded_queue` |
| Thread pool | `concurrency/thread_pool` |
| Read-write lock | `concurrency/read_write_lock` |
| In-process distributed lock | `concurrency/in_process_lock` |

## Messaging and time

| Topic | Path |
| ----- | ---- |
| In-memory pub-sub | `messaging/pub_sub` |
| Delayed job queue | `messaging/delayed_queue` |
| Task scheduler | `messaging/scheduler` |
| Multi-level logger | `messaging/logger` |

## APIs

| Topic | Path |
| ----- | ---- |
| URL shortener | `apis/url_shortener` |
| Wallet and ledger | `apis/wallet` |
| Expense split | `apis/expense_split` |
| Autocomplete | `apis/autocomplete` |

## Object design

| Topic | Path |
| ----- | ---- |
| Parking lot | `object_design/parking_lot` |
| Elevator | `object_design/elevator` |
| Vending machine | `object_design/vending_machine` |
| Movie ticket booking | `object_design/movie_booking` |
| Snake and ladder | `object_design/snake_ladder` |
| Library checkout | `object_design/library` |

Run any example from its folder:

```bash
python main.py
```
