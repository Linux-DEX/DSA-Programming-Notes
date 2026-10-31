import time


class LeakyBucket:
    """
    Rate limiter that drips at a fixed rate.

    `allow(amount)` adds water. If the bucket would pass `capacity`,
    the request is rejected and the water level is left unchanged.
    Water leaks continuously at `leak_per_second`.

    This is the dual of the token bucket in rate_limiter/token_bucket.py:
    tokens refill, water here drains.
    """

    def __init__(self, capacity, leak_per_second):
        if capacity <= 0 or leak_per_second <= 0:
            raise ValueError("capacity and leak_per_second must be positive")
        self.capacity = capacity
        self.leak_per_second = leak_per_second
        self.water = 0.0
        self._last = time.monotonic()

    def allow(self, amount):
        self._leak()
        if amount <= 0:
            raise ValueError("amount must be positive")
        if self.water + amount > self.capacity:
            return False
        self.water += amount
        return True

    def _leak(self):
        now = time.monotonic()
        elapsed = now - self._last
        self._last = now
        self.water = max(0.0, self.water - elapsed * self.leak_per_second)
