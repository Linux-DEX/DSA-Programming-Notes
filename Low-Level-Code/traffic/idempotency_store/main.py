import threading

from idempotency_store import IdempotencyStore


def main():
    store = IdempotencyStore()
    calls = {"n": 0}

    def charge():
        calls["n"] += 1
        return {"status": "charged", "amount": 40}

    first = store.execute("pay-1", charge)
    second = store.execute("pay-1", charge)
    print("first:", first)
    print("second:", second, "calls:", calls["n"])
    assert first == second == {"status": "charged", "amount": 40}
    assert calls["n"] == 1

    started = threading.Event()
    release = threading.Event()

    def slow():
        started.set()
        release.wait()
        return "done"

    holder = threading.Thread(target=lambda: store.execute("pay-2", slow))
    holder.start()
    started.wait()
    try:
        store.execute("pay-2", slow)
        raise AssertionError("overlapping call must fail")
    except RuntimeError as exc:
        print("overlap:", exc)
    release.set()
    holder.join()
    assert store.execute("pay-2", lambda: "other") == "done"


if __name__ == "__main__":
    main()
