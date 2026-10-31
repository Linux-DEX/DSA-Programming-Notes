import threading

from thread_pool import ThreadPool


def main():
    pool = ThreadPool(worker_count=2)
    results = []
    lock = threading.Lock()

    def add(value):
        with lock:
            results.append(value)

    for value in range(4):
        pool.submit(add, (value,))
    pool.shutdown()
    print("results:", sorted(results))
    assert sorted(results) == [0, 1, 2, 3]

    try:
        pool.submit(add, (9,))
        raise AssertionError("submit after shutdown must fail")
    except RuntimeError as exc:
        print("after shutdown:", exc)


if __name__ == "__main__":
    main()
