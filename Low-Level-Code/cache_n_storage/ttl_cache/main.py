import time

from ttl_cache import TTLCache


def main():
    cache = TTLCache(capacity=3, default_ttl=5)

    # Insert entries.
    cache.put("A", "Apple", ttl=10)
    cache.put("B", "Banana", ttl=3)
    cache.put("C", "Cherry", ttl=10)

    cache.display()

    # Access A to make it most recently used.
    print("\nGet A:", cache.get("A"))

    # Wait for B to expire.
    print("\nWaiting for B to expire...")
    time.sleep(4)

    # B should return -1.
    print("Get B:", cache.get("B"))

    cache.display()

    # Insert D.
    # B has expired and will be removed during cleanup.
    cache.put("D", "Date", ttl=10)

    cache.display()

    # Fill cache again.
    cache.put("E", "Elderberry", ttl=10)

    # Cache is full. The least recently used valid entry
    # will be evicted.
    cache.put("F", "Fig", ttl=10)

    cache.display()

    print("\nFinal cache size:", cache.size())


if __name__ == "__main__":
    main()
