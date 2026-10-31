class Node:
    """
    Represents one cache entry.

    Attributes:
        key: Cache key.
        value: Cache value.
        prev: Previous node.
        next: Next node.
    """

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
