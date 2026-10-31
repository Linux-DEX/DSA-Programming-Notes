import queue


class Connection:
    """Stand-in for a socket or database session. The pool owns reuse, not I/O."""

    def __init__(self, conn_id):
        self.conn_id = conn_id

    def execute(self, query):
        return f"ok:{self.conn_id}:{query}"


class ConnectionPool:
    """
    Fixed set of connections. acquire waits up to timeout seconds.
    release returns a connection to the pool.

    ponytail: connections are created up front and never replaced.
    A pool that talks to a real server would also health-check and reconnect.
    """

    def __init__(self, size):
        if size <= 0:
            raise ValueError("size must be positive")
        self._pool = queue.Queue(maxsize=size)
        for conn_id in range(size):
            self._pool.put(Connection(conn_id))

    def acquire(self, timeout):
        try:
            return self._pool.get(timeout=timeout)
        except queue.Empty:
            raise TimeoutError("pool exhausted")

    def release(self, conn):
        try:
            self._pool.put_nowait(conn)
        except queue.Full:
            raise RuntimeError("connection does not belong to this pool")
