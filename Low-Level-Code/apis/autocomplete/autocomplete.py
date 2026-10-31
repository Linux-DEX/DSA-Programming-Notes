class _Node:
    def __init__(self):
        self.children = {}
        self.word = None
        self.freq = 0


class Autocomplete:
    """
    Trie of words with a frequency on each complete word.

    suggest(prefix, k) returns up to k completions, highest frequency first.
    Equal frequencies are ordered by the word.

    ponytail: suggest walks the whole subtree, then sorts.
    Store a top-k list on each node when the dictionary is large.
    """

    def __init__(self):
        self._root = _Node()

    def insert(self, word, freq):
        if not word or freq <= 0:
            raise ValueError("word must be non-empty and freq must be positive")
        node = self._root
        for char in word:
            node = node.children.setdefault(char, _Node())
        node.word = word
        node.freq += freq

    def suggest(self, prefix, k):
        if k <= 0:
            raise ValueError("k must be positive")
        node = self._root
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return []
        found = []
        self._collect(node, found)
        found.sort(key=lambda item: (-item[0], item[1]))
        return [word for _freq, word in found[:k]]

    def _collect(self, node, found):
        if node.word is not None:
            found.append((node.freq, node.word))
        for child in node.children.values():
            self._collect(child, found)
