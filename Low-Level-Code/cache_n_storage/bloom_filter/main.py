from bloom_filter import BloomFilter


def main():
    bloom = BloomFilter(size=20_000, hash_count=4)
    for word in ("cache", "queue", "lock"):
        bloom.add(word)

    print("cache:", bloom.might_contain("cache"))
    print("elevator:", bloom.might_contain("elevator"))
    assert bloom.might_contain("cache")
    assert bloom.might_contain("queue")
    assert bloom.might_contain("lock")
    assert not bloom.might_contain("elevator")

    tiny = BloomFilter(size=32, hash_count=3)
    tiny.add("cat")
    false_positive = None
    for i in range(400):
        word = f"w{i}"
        if tiny.might_contain(word):
            false_positive = word
            break
    print("false positive from a tiny filter:", false_positive)


if __name__ == "__main__":
    main()
