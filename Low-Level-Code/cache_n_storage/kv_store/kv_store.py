import time


class KVStore:
    """
    In-memory key-value store.

    set(key, value, ttl) stores a value. ttl is seconds, or None for no expiry.
    get and ttl drop a key once its deadline has passed (lazy expiration).

    ttl() follows the Redis convention:
        > 0  seconds left
        -1   key exists and does not expire
        -2   key is missing

    ponytail: expired keys stay until the next get, delete, or ttl.
    A background sweep is the upgrade when the key set is large and cold.
    """

    def __init__(self):
        self._data = {}

    def set(self, key, value, ttl):
        expire_at = None if ttl is None else time.monotonic() + ttl
        self._data[key] = (value, expire_at)

    def get(self, key):
        item = self._live(key)
        if item is None:
            return None
        return item[0]

    def delete(self, key):
        self._live(key)
        return self._data.pop(key, None) is not None

    def ttl(self, key):
        item = self._live(key)
        if item is None:
            return -2
        expire_at = item[1]
        if expire_at is None:
            return -1
        return expire_at - time.monotonic()

    def _live(self, key):
        item = self._data.get(key)
        if item is None:
            return None
        expire_at = item[1]
        if expire_at is not None and time.monotonic() >= expire_at:
            del self._data[key]
            return None
        return item
