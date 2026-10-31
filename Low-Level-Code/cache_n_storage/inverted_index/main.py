from inverted_index import InvertedIndex


def main():
    index = InvertedIndex()
    index.add(1, "Cache eviction uses frequency and recency")
    index.add(2, "A bloom filter answers set membership")
    index.add(3, "Cache and bloom filter notes")

    print("cache:", index.search("cache"))
    print("bloom filter:", index.search("bloom filter"))
    print("missing:", index.search("elevator"))

    assert index.search("cache") == [1, 3]
    assert index.search("bloom filter") == [2, 3]
    assert index.search("elevator") == []

    index.add(1, "Only locks in this rewrite")
    print("doc 1 rewritten, cache:", index.search("cache"))
    assert index.search("cache") == [3]
    assert index.search("locks") == [1]


if __name__ == "__main__":
    main()
