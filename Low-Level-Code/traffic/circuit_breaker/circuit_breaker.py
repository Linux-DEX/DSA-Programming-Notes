import time


class CircuitOpenError(Exception):
    """Raised when the breaker rejects a call without running it."""


class CircuitBreaker:
    """
    Stop calling a failing dependency, then try one probe after a cool-down.

    closed    -> calls go through; failures count
    open      -> calls are rejected until reset_timeout
    half_open -> the next call is the probe
                 success closes the breaker
                 failure opens it again
    """

    def __init__(self, failure_threshold, reset_timeout):
        if failure_threshold <= 0 or reset_timeout <= 0:
            raise ValueError("failure_threshold and reset_timeout must be positive")
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.state = "closed"
        self._failures = 0
        self._opened_at = None

    def call(self, func):
        self._before()
        try:
            result = func()
        except Exception:
            self._on_failure()
            raise
        self._on_success()
        return result

    def _before(self):
        if self.state != "open":
            return
        if time.monotonic() - self._opened_at >= self.reset_timeout:
            self.state = "half_open"
            return
        raise CircuitOpenError("circuit open")

    def _on_success(self):
        self._failures = 0
        self.state = "closed"
        self._opened_at = None

    def _on_failure(self):
        self._failures += 1
        if self.state == "half_open" or self._failures >= self.failure_threshold:
            self.state = "open"
            self._opened_at = time.monotonic()
