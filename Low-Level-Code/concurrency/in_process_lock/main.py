import time

from in_process_lock import InProcessLock, LockError


def main():
    locks = InProcessLock()
    first = locks.acquire("db", "a", 1.0)
    second = locks.acquire("db", "b", 1.0)
    print("tokens:", first, second)
    assert first is not None
    assert second is None

    locks.release("db", "a", first)
    third = locks.acquire("db", "b", 1.0)
    print("after release:", third)
    assert third is not None and third != first

    try:
        locks.release("db", "b", first)
        raise AssertionError("old token must not release the lock")
    except LockError as exc:
        print("stale token:", exc)

    locks.release("db", "b", third)

    short = locks.acquire("job", "a", 0.02)
    time.sleep(0.04)
    taken = locks.acquire("job", "b", 1.0)
    print("expired lease taken by b:", taken)
    assert short is not None and taken is not None
    locks.release("job", "b", taken)


if __name__ == "__main__":
    main()
