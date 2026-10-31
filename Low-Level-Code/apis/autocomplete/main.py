from autocomplete import Autocomplete


def main():
    trie = Autocomplete()
    trie.insert("app", 10)
    trie.insert("apple", 5)
    trie.insert("application", 3)
    trie.insert("banana", 8)
    trie.insert("apple", 6)

    print("app:", trie.suggest("app", 2))
    print("ban:", trie.suggest("ban", 5))
    print("z:", trie.suggest("z", 3))
    assert trie.suggest("app", 2) == ["apple", "app"]
    assert trie.suggest("ban", 5) == ["banana"]
    assert trie.suggest("z", 3) == []


if __name__ == "__main__":
    main()
