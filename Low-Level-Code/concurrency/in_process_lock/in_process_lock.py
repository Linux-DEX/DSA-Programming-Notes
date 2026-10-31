import threading
import time


class LockError(Exception):
    """Raised when release or renew does not match the current owner and token."""


class InProcessLock:
    """
    Lease lock with an owner and a fencing token.

    Several threads share one process, using the same rules as a
    distributed lock: only the owner can release, a lease expires,
    and each successful acquire gets a new token. A stale owner
    holding an old token cannot unlock or renew.

    ponytail: the lease table is in memory. A real lock lives in
    a store the other processes can see.
    """

    def __init__(self):
        self._mu = threading.Lock()
        self._locks = {}
        self._next_token = 1

    def acquire(self, name, owner, ttl):
        if ttl <= 0:
            raise ValueError("ttl must be positive")
        now = time.monotonic()
        with self._mu:
            current = self._locks.get(name)
            held = current is not None and current["expires"] > now
            if held and current["owner"] != owner:
                return None
            token = self._next_token
            self._next_token += 1
            self._locks[name] = {
                "owner": owner,
                "token": token,
                "expires": now + ttl,
            }
            return token

    def release(self, name, owner, token):
        with self._mu:
            self._require(name, owner, token)
            del self._locks[name]

    def renew(self, name, owner, token, ttl):
        if ttl <= 0:
            raise ValueError("ttl must be positive")
        now = time.monotonic()
        with self._mu:
            current = self._require(name, owner, token)
            if current["expires"] <= now:
                del self._locks[name]
                raise LockError("lease expired")
            current["expires"] = now + ttl

    def _require(self, name, owner, token):
        current = self._locks.get(name)
        if current is None or current["owner"] != owner or current["token"] != token:
            raise LockError("not lock owner")
        return current
