import time

from circuit_breaker import CircuitBreaker, CircuitOpenError


def main():
    calls = {"n": 0}

    def fail():
        calls["n"] += 1
        raise RuntimeError("dependency down")

    breaker = CircuitBreaker(failure_threshold=2, reset_timeout=0.05)
    for _ in range(2):
        try:
            breaker.call(fail)
        except RuntimeError as exc:
            print("failure:", exc)

    print("state:", breaker.state)
    assert breaker.state == "open"

    try:
        breaker.call(fail)
        raise AssertionError("open circuit must reject the call")
    except CircuitOpenError as exc:
        print("rejected:", exc)
    assert calls["n"] == 2

    time.sleep(0.06)

    def ok():
        return "up"

    print("probe:", breaker.call(ok))
    print("state:", breaker.state)
    assert breaker.state == "closed"

    probe = CircuitBreaker(failure_threshold=1, reset_timeout=0.05)
    try:
        probe.call(fail)
    except RuntimeError:
        pass
    time.sleep(0.06)
    try:
        probe.call(fail)
    except RuntimeError:
        print("half-open probe failed, state:", probe.state)
    assert probe.state == "open"


if __name__ == "__main__":
    main()
