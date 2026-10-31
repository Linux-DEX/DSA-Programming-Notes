from doubly_linked_list import DoublyLinkedList


class FrequencyMap:
    """
    Maps an access frequency to a doubly linked list.

    Each frequency maintains its own LRU ordering.
    """

    def __init__(self):
        self.store = {}

    def get_list(self, frequency):
        """Get the linked list for a frequency."""

        if frequency not in self.store:
            self.store[frequency] = DoublyLinkedList()

        return self.store[frequency]

    def remove_empty_list(self, frequency):
        """Remove a frequency bucket if it becomes empty."""

        linked_list = self.store.get(frequency)

        if linked_list and linked_list.is_empty():
            del self.store[frequency]

    def contains(self, frequency):
        return frequency in self.store

    def get_frequencies(self):
        return list(self.store.keys())
