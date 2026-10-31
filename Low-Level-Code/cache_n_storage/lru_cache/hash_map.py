class HashMap:
    """
    Maps cache keys to their corresponding nodes.
    """

    def __init__(self):
        self.store = {}

    def put(self, key, node):
        """Insert or update a key-node pair."""

        self.store[key] = node

    def get(self, key):
        """Return the node associated with a key."""

        return self.store.get(key)

    def remove(self, key):
        """Remove a key and return its associated node."""

        return self.store.pop(key, None)

    def contains(self, key):
        """Check whether a key exists."""

        return key in self.store

    def size(self):
        return len(self.store)

    def is_empty(self):
        return len(self.store) == 0
