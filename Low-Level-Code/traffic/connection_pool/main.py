from connection_pool import ConnectionPool


def main():
    pool = ConnectionPool(size=1)
    first = pool.acquire(timeout=0.1)
    print(first.execute("select 1"))

    try:
        pool.acquire(timeout=0.05)
        raise AssertionError("second acquire must time out")
    except TimeoutError as exc:
        print("exhausted:", exc)

    pool.release(first)
    second = pool.acquire(timeout=0.1)
    print("reused:", second.conn_id)
    assert second.conn_id == first.conn_id
    assert second.execute("select 2") == "ok:0:select 2"
    pool.release(second)


if __name__ == "__main__":
    main()
