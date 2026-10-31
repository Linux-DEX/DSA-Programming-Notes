from node import Node
from hash_map import HashMap
from frequency_map import FrequencyMap


class LFUCache:
    """
    LFU (Least Frequently Used) Cache.

    Eviction policy:
        1. Evict the entry with the lowest frequency.
        2. If multiple entries have the same frequency,
           evict the least recently used entry.

    Average time complexity:
        get()  -> O(1)
        put()  -> O(1)
    """

    def __init__(self, capacity):
        self.capacity = capacity

        self.hash_map = HashMap()
        self.frequency_map = FrequencyMap()

        self.min_frequency = 0

    def get(self, key):
        """Retrieve a value and update its frequency."""

        node = self.hash_map.get(key)

        if node is None:
            return -1

        self._increase_frequency(node)

        return node.value

    def put(self, key, value):
        """Insert or update a cache entry."""

        if self.capacity <= 0:
            return

        # Update an existing entry.
        existing_node = self.hash_map.get(key)

        if existing_node is not None:
            existing_node.value = value
            self._increase_frequency(existing_node)
            return

        # Evict an entry if the cache is full.
        if self.hash_map.size() >= self.capacity:
            self._evict()

        # Insert a new entry with frequency 1.
        node = Node(key, value)

        self.hash_map.put(key, node)

        self.frequency_map.get_list(1).add_to_front(node)

        self.min_frequency = 1

    def _increase_frequency(self, node):
        """Move a node from frequency f to frequency f + 1."""

        current_frequency = node.frequency

        current_list = self.frequency_map.get_list(current_frequency)
        current_list.remove_node(node)

        self.frequency_map.remove_empty_list(current_frequency)

        # Update minimum frequency if its bucket became empty.
        if current_frequency == self.min_frequency and current_list.is_empty():
            self.min_frequency += 1

        node.frequency += 1

        new_list = self.frequency_map.get_list(node.frequency)
        new_list.add_to_front(node)

    def _evict(self):
        """Evict the LRU node from the minimum frequency bucket."""

        lru_list = self.frequency_map.get_list(self.min_frequency)

        node = lru_list.remove_last()

        if node is None:
            return

        self.hash_map.remove(node.key)

        self.frequency_map.remove_empty_list(self.min_frequency)

    def display(self):
        """Display current cache contents."""

        print("\nCache contents:")

        for key, node in self.hash_map.store.items():
            print(f"Key: {key}, Value: {node.value}, Frequency: {node.frequency}")

        print(f"Minimum frequency: {self.min_frequency}")
