from lru_cache import LRUCache


def main():
    cache = LRUCache(capacity=3)

    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")

    cache.display()

    # Access key 1, making it the most recently used.
    print("\nGet key 1:", cache.get(1))

    cache.display()

    # Access key 2.
    print("\nGet key 2:", cache.get(2))

    cache.display()

    # Insert key 4.
    # Key 3 is now the least recently used and gets evicted.
    cache.put(4, "D")

    cache.display()

    print("\nGet key 3:", cache.get(3))
    print("Get key 4:", cache.get(4))


if __name__ == "__main__":
    main()
