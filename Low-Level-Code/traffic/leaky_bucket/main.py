import time

from leaky_bucket import LeakyBucket


def main():
    bucket = LeakyBucket(capacity=2, leak_per_second=50)

    results = [bucket.allow(1) for _ in range(3)]
    print("allows:", results)
    assert results == [True, True, False]

    time.sleep(0.05)
    allowed = bucket.allow(1)
    print("after leak:", allowed)
    assert allowed is True


if __name__ == "__main__":
    main()
