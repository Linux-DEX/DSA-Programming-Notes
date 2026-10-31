class HashMap:
    """
    Maps cache keys to their corresponding nodes.
    """

    def __init__(self):
        self.store = {}

    def put(self, key, node):
        self.store[key] = node

    def get(self, key):
        return self.store.get(key)

    def remove(self, key):
        return self.store.pop(key, None)

    def contains(self, key):
        return key in self.store

    def size(self):
        return len(self.store)

    def is_empty(self):
        return len(self.store) == 0

    def keys(self):
        return list(self.store.keys())
