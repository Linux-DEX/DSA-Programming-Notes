import threading


class IdempotencyStore:
    """
    Run a unit of work once per key.

    The first caller marks the key running, runs func, and stores the result.
    A later caller with the same key gets that result and does not run func.
    A caller that arrives while the first is still inside func gets an error.
    A failed func clears the key so a later attempt can run it.

    ponytail: the map lives in this process. Restarting loses completed keys.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._records = {}

    def execute(self, key, func):
        with self._lock:
            record = self._records.get(key)
            if record is not None and record["state"] == "done":
                return record["result"]
            if record is not None and record["state"] == "running":
                raise RuntimeError("request in progress")
            self._records[key] = {"state": "running", "result": None}
        try:
            result = func()
        except Exception:
            with self._lock:
                current = self._records.get(key)
                if current is not None and current["state"] == "running":
                    del self._records[key]
            raise
        with self._lock:
            self._records[key] = {"state": "done", "result": result}
        return result
