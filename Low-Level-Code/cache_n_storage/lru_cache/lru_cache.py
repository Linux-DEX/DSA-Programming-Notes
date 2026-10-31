from node import Node
from hash_map import HashMap
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    LRU (Least Recently Used) Cache.

    Eviction policy:
        1. Most recently used entries stay at the front.
        2. Least recently used entries stay at the back.
        3. When full, evict the node at the back.

    Average time complexity:
        get()  -> O(1)
        put()  -> O(1)
    """

    def __init__(self, capacity):
        self.capacity = capacity

        self.hash_map = HashMap()
        self.dll = DoublyLinkedList()

    def get(self, key):
        """Retrieve a value and mark it as recently used."""

        node = self.hash_map.get(key)

        if node is None:
            return -1

        # Move accessed node to the front.
        self.dll.move_to_front(node)

        return node.value

    def put(self, key, value):
        """Insert or update a cache entry."""

        if self.capacity <= 0:
            return

        existing_node = self.hash_map.get(key)

        # Update existing entry.
        if existing_node is not None:
            existing_node.value = value

            # Updating also makes it recently used.
            self.dll.move_to_front(existing_node)
            return

        # Evict LRU entry if cache is full.
        if self.hash_map.size() >= self.capacity:
            self._evict()

        # Create and insert new entry.
        node = Node(key, value)

        self.hash_map.put(key, node)
        self.dll.add_to_front(node)

    def _evict(self):
        """Remove the least recently used entry."""

        node = self.dll.remove_last()

        if node is not None:
            self.hash_map.remove(node.key)

    def display(self):
        """Display cache entries from MRU to LRU."""

        print("\nCache contents (MRU -> LRU):")

        current = self.dll.head.next

        while current != self.dll.tail:
            print(f"Key: {current.key}, Value: {current.value}")

            current = current.next

        print(f"Cache size: {self.dll.get_size()}")
