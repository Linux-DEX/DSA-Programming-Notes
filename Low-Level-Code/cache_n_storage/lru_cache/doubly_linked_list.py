from node import Node


class DoublyLinkedList:
    """
    Doubly linked list with sentinel head and tail nodes.

    New or recently accessed nodes are moved to the front.
    The least recently used node is removed from the back.
    """

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_to_front(self, node):
        """Insert a node at the front of the list."""

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove_node(self, node):
        """Remove a specific node from the list."""

        if node is self.head or node is self.tail:
            raise ValueError("Cannot remove sentinel nodes")

        if node.prev is None or node.next is None:
            raise ValueError("Node is not currently linked")

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

        self.size -= 1

    def move_to_front(self, node):
        """Move an existing node to the MRU position."""

        self.remove_node(node)
        self.add_to_front(node)

    def remove_last(self):
        """Remove and return the LRU node."""

        if self.is_empty():
            return None

        node = self.tail.prev
        self.remove_node(node)

        return node

    def get_first(self):
        """Return the MRU node without removing it."""

        if self.is_empty():
            return None

        return self.head.next

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
