import hashlib


class BloomFilter:
    """
    Probabilistic set.

    add(item) inserts. might_contain(item) is never a false negative.
    It can be a false positive: a missing item can still look present.

    Two hashes are mixed as h1 + i * h2 so each item sets hash_count bits.

    ponytail: one byte per bit. Pack the bits if the filter is large.
    """

    def __init__(self, size, hash_count):
        if size <= 0 or hash_count <= 0:
            raise ValueError("size and hash_count must be positive")
        self.size = size
        self.hash_count = hash_count
        self.bits = bytearray(size)

    def add(self, item):
        for index in self._indexes(item):
            self.bits[index] = 1

    def might_contain(self, item):
        return all(self.bits[index] for index in self._indexes(item))

    def _indexes(self, item):
        data = str(item).encode()
        h1 = int.from_bytes(hashlib.md5(data).digest(), "big")
        h2 = int.from_bytes(hashlib.sha256(data).digest(), "big")
        for i in range(self.hash_count):
            yield (h1 + i * h2) % self.size
