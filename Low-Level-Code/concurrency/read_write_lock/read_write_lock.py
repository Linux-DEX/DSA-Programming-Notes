import threading


class ReadWriteLock:
    """
    Many readers, or one writer.

    A waiting writer blocks new readers so writers are not starved
    by a stream of reads.
    """

    def __init__(self):
        self._cond = threading.Condition()
        self._readers = 0
        self._writer = False
        self._waiting_writers = 0

    def acquire_read(self):
        with self._cond:
            while self._writer or self._waiting_writers:
                self._cond.wait()
            self._readers += 1

    def release_read(self):
        with self._cond:
            if self._readers <= 0:
                raise RuntimeError("no read lock held")
            self._readers -= 1
            if self._readers == 0:
                self._cond.notify_all()

    def acquire_write(self):
        with self._cond:
            self._waiting_writers += 1
            while self._writer or self._readers:
                self._cond.wait()
            self._waiting_writers -= 1
            self._writer = True

    def release_write(self):
        with self._cond:
            if not self._writer:
                raise RuntimeError("no write lock held")
            self._writer = False
            self._cond.notify_all()
