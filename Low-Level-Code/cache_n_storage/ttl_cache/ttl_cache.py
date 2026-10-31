import time

from node import Node
from hash_map import HashMap
from doubly_linked_list import DoublyLinkedList


class TTLCache:
    """
    TTL Cache with LRU eviction.

    Features:
        - Each entry has an expiration time.
        - Expired entries are not returned.
        - Expired entries are cleaned up during get/put.
        - LRU eviction is used when capacity is reached.

    Average time complexity:
        get()       -> O(1)
        put()       -> O(n) because of expired-entry cleanup
        delete()    -> O(1)
        eviction    -> O(1)
    """

    def __init__(self, capacity, default_ttl=None):
        self.capacity = capacity
        self.default_ttl = default_ttl

        self.hash_map = HashMap()
        self.dll = DoublyLinkedList()

    def put(self, key, value, ttl=None):
        """
        Insert or update a cache entry.

        Args:
            key: Cache key.
            value: Cache value.
            ttl: Expiration duration in seconds.
                 Uses default_ttl when omitted.
        """

        if self.capacity <= 0:
            return

        if ttl is None:
            ttl = self.default_ttl

        if ttl is None:
            raise ValueError("TTL must be provided")

        if ttl <= 0:
            self.delete(key)
            return

        # Remove expired entries before insertion.
        self.cleanup_expired()

        expires_at = time.monotonic() + ttl

        existing_node = self.hash_map.get(key)

        # Update an existing entry.
        if existing_node is not None:
            existing_node.value = value
            existing_node.expires_at = expires_at

            self.dll.move_to_front(existing_node)
            return

        # Evict LRU entry if cache is full.
        if self.hash_map.size() >= self.capacity:
            self._evict_lru()

        # Insert new entry.
        node = Node(key=key, value=value, expires_at=expires_at)

        self.hash_map.put(key, node)
        self.dll.add_to_front(node)

    def get(self, key):
        """Retrieve a value if it has not expired."""

        node = self.hash_map.get(key)

        if node is None:
            return -1

        # Check expiration.
        if self._is_expired(node):
            self._remove_node(node)
            return -1

        # Mark entry as recently used.
        self.dll.move_to_front(node)

        return node.value

    def delete(self, key):
        """Delete an entry manually."""

        node = self.hash_map.get(key)

        if node is None:
            return False

        self._remove_node(node)
        return True

    def cleanup_expired(self):
        """
        Scan all entries and remove expired entries.

        Time complexity: O(n).
        """

        current = self.dll.head.next
        current_time = time.monotonic()

        removed_count = 0

        while current != self.dll.tail:
            next_node = current.next

            if current.expires_at <= current_time:
                self._remove_node(current)
                removed_count += 1

            current = next_node

        return removed_count

    def _is_expired(self, node):
        """Check whether an entry has expired."""

        return time.monotonic() >= node.expires_at

    def _remove_node(self, node):
        """Remove node from both data structures."""

        self.dll.remove_node(node)
        self.hash_map.remove(node.key)

    def _evict_lru(self):
        """Evict the least recently used entry."""

        node = self.dll.remove_last()

        if node is not None:
            self.hash_map.remove(node.key)

    def size(self):
        """Return the current number of stored entries."""

        return self.hash_map.size()

    def display(self):
        """Display cache entries from MRU to LRU."""

        print("\nCache contents (MRU -> LRU):")

        current = self.dll.head.next
        current_time = time.monotonic()

        while current != self.dll.tail:
            remaining_ttl = max(0, current.expires_at - current_time)

            print(
                f"Key: {current.key}, "
                f"Value: {current.value}, "
                f"Remaining TTL: {remaining_ttl:.2f}s"
            )

            current = current.next

        print(f"Cache size: {self.size()}")
