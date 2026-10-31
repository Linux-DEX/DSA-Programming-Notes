from lfu_cache import LFUCache


def main():
    cache = LFUCache(capacity=3)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")

    cache.get(1)
    cache.get(1)
    cache.get(2)

    cache.display()

    # Cache is full. Key 3 has the lowest frequency,
    # so it will be evicted.
    cache.put(4, "D")

    cache.display()

    print("\nGet key 1:", cache.get(1))
    print("Get key 3:", cache.get(3))
    print("Get key 4:", cache.get(4))


if __name__ == "__main__":
    main()
