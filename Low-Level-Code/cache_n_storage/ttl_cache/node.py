class Node:
    """
    Represents a cache entry.

    Attributes:
        key: Cache key.
        value: Cache value.
        expires_at: Monotonic timestamp when entry expires.
        prev: Previous node.
        next: Next node.
    """

    def __init__(self, key=None, value=None, expires_at=None):
        self.key = key
        self.value = value
        self.expires_at = expires_at

        self.prev = None
        self.next = None
