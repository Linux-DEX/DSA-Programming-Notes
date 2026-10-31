import time

from kv_store import KVStore


def main():
    store = KVStore()
    store.set("a", 1, None)
    store.set("b", 2, 0.02)

    print("get a:", store.get("a"))
    print("ttl a:", store.ttl("a"))
    print("get b:", store.get("b"))

    assert store.get("a") == 1
    assert store.ttl("a") == -1
    assert store.get("b") == 2
    assert store.ttl("b") > 0

    time.sleep(0.03)

    print("get b after ttl:", store.get("b"))
    print("ttl b after expiry:", store.ttl("b"))
    assert store.get("b") is None
    assert store.ttl("b") == -2

    assert store.delete("a") is True
    assert store.get("a") is None
    assert store.delete("a") is False
    print("delete a: removed, second delete is a no-op")


if __name__ == "__main__":
    main()
