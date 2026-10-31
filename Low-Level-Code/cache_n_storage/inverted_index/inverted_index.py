import re
from collections import defaultdict


class InvertedIndex:
    """
    Word -> set of document ids.

    search() keeps documents that contain every query word (AND).

    ponytail: posting lists are Python sets. A production index stores
    sorted lists so it can intersect without hashing every id.
    """

    def __init__(self):
        self._index = defaultdict(set)
        self._docs = {}

    def add(self, doc_id, text):
        previous = self._docs.get(doc_id)
        if previous is not None:
            for token in self._tokens(previous):
                self._index[token].discard(doc_id)
        self._docs[doc_id] = text
        for token in self._tokens(text):
            self._index[token].add(doc_id)

    def search(self, query):
        tokens = self._tokens(query)
        if not tokens:
            return []
        hits = None
        for token in tokens:
            posting = self._index.get(token, set())
            hits = set(posting) if hits is None else hits & posting
        return sorted(hits)

    def _tokens(self, text):
        return set(re.findall(r"[a-z0-9]+", text.lower()))
