from retry_backoff import retry


def main():
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise TimeoutError("timeout")
        return "ok"

    result = retry(flaky, attempts=5, base_delay=0.01, max_delay=0.05)
    print("result:", result, "calls:", calls["n"])
    assert result == "ok"
    assert calls["n"] == 3

    def down():
        raise RuntimeError("still down")

    try:
        retry(down, attempts=2, base_delay=0.001, max_delay=0.002)
        raise AssertionError("retry must raise the last error")
    except RuntimeError as exc:
        print("gave up:", exc)
        assert str(exc) == "still down"


if __name__ == "__main__":
    main()
