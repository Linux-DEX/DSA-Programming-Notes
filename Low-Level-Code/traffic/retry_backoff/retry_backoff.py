import random
import time


def retry(func, attempts, base_delay, max_delay):
    """
    Call func until it returns or attempts run out.

    Sleep before each retry is full jitter: uniform(0, min(max_delay, base * 2^n)).
    The last exception is raised unchanged.
    """
    if attempts <= 0 or base_delay < 0 or max_delay < 0:
        raise ValueError("attempts must be positive and delays must be >= 0")

    last_error = None
    for attempt in range(attempts):
        try:
            return func()
        except Exception as exc:
            last_error = exc
            if attempt == attempts - 1:
                break
            cap = min(max_delay, base_delay * (2 ** attempt))
            time.sleep(random.uniform(0, cap))
    raise last_error
