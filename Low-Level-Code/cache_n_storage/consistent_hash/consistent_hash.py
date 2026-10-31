import bisect
import hashlib


class ConsistentHashRing:
    """
    Map a key to a node, and move only the keys on a removed node's arc.

    Each physical node owns `virtual_nodes` points on the ring so the
    spread stays even when nodes come and go.

    ponytail: the ring is a sorted list. Fine for dozens of nodes.
    A tree map is the upgrade when nodes are added and removed constantly.
    """

    def __init__(self, virtual_nodes):
        if virtual_nodes <= 0:
            raise ValueError("virtual_nodes must be positive")
        self.virtual_nodes = virtual_nodes
        self._ring = []
        self._nodes = {}
        self._members = set()

    def add_node(self, node):
        if node in self._members:
            return
        self._members.add(node)
        for i in range(self.virtual_nodes):
            point = self._hash(f"{node}#{i}")
            if point in self._nodes:
                continue
            bisect.insort(self._ring, point)
            self._nodes[point] = node

    def remove_node(self, node):
        if node not in self._members:
            return
        self._members.remove(node)
        for i in range(self.virtual_nodes):
            point = self._hash(f"{node}#{i}")
            index = bisect.bisect_left(self._ring, point)
            if index < len(self._ring) and self._ring[index] == point and self._nodes.get(point) == node:
                self._ring.pop(index)
                del self._nodes[point]

    def get_node(self, key):
        if not self._ring:
            return None
        point = self._hash(key)
        index = bisect.bisect_left(self._ring, point) % len(self._ring)
        return self._nodes[self._ring[index]]

    def _hash(self, key):
        digest = hashlib.md5(str(key).encode()).digest()
        return int.from_bytes(digest, "big")
