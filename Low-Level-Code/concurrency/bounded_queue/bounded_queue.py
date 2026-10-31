import threading
from collections import deque


class BoundedBlockingQueue:
    """
    FIFO queue. put blocks while the queue is at capacity.
    get blocks while it is empty.

    ponytail: waiters wake with notify_all. A pair of conditions
    (not_full, not_empty) is the upgrade when many threads block.
    """

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._items = deque()
        self._cond = threading.Condition()

    def put(self, item):
        with self._cond:
            while len(self._items) >= self.capacity:
                self._cond.wait()
            self._items.append(item)
            self._cond.notify_all()

    def get(self):
        with self._cond:
            while not self._items:
                self._cond.wait()
            item = self._items.popleft()
            self._cond.notify_all()
            return item
