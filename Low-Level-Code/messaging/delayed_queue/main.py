import time

from delayed_queue import DelayedQueue


def main():
    queue = DelayedQueue()
    now = time.monotonic()
    queue.schedule(now + 0.05, "later")
    queue.schedule(now, "now")

    first = queue.get()
    second = queue.get()
    print("jobs:", first, second)
    assert first == "now"
    assert second == "later"

    queue.close()
    assert queue.get() is None


if __name__ == "__main__":
    main()
