import heapq
import threading
import time


class DelayedQueue:
    """
    Jobs become available at a monotonic timestamp.

    get() waits until the earliest job is due, then returns it.

    ponytail: the heap is in memory. A restart drops every scheduled job.
    """

    def __init__(self):
        self._heap = []
        self._seq = 0
        self._cond = threading.Condition()
        self._closed = False

    def schedule(self, run_at, job):
        with self._cond:
            if self._closed:
                raise RuntimeError("queue closed")
            heapq.heappush(self._heap, (run_at, self._seq, job))
            self._seq += 1
            self._cond.notify()

    def get(self):
        with self._cond:
            while True:
                if not self._heap:
                    if self._closed:
                        return None
                    self._cond.wait()
                    continue
                run_at, _, job = self._heap[0]
                wait = run_at - time.monotonic()
                if wait > 0:
                    self._cond.wait(timeout=wait)
                    continue
                heapq.heappop(self._heap)
                return job

    def close(self):
        with self._cond:
            self._closed = True
            self._cond.notify_all()
