import threading

from booking import Cinema


def main():
    cinema = Cinema()
    cinema.add_show("evening", ["A1", "A2", "A3"])
    booked = cinema.book("evening", ["A1", "A2"])
    print("booked:", booked)
    print("left:", cinema.shows["evening"].available())
    assert booked == ["A1", "A2"]
    assert cinema.shows["evening"].available() == ["A3"]

    try:
        cinema.book("evening", ["A2", "A3"])
        raise AssertionError("a taken seat must reject the whole booking")
    except ValueError as exc:
        print("conflict:", exc)
    assert cinema.shows["evening"].available() == ["A3"]

    results = []

    def grab():
        try:
            cinema.book("evening", ["A3"])
            results.append("ok")
        except ValueError:
            results.append("no")

    threads = [threading.Thread(target=grab) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("race:", results)
    assert sorted(results) == ["no", "ok"]
    assert cinema.shows["evening"].available() == []


if __name__ == "__main__":
    main()
