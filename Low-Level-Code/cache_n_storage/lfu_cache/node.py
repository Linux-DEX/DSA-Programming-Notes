class Node:
    """
    Represents a single cache entry.
    """

    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev = None
        self.next = None
