import time

from scheduler import Scheduler


def main():
    scheduler = Scheduler()
    fired = []

    def once():
        fired.append("once")

    def tick():
        fired.append("tick")

    scheduler.at(time.monotonic() + 0.02, once)
    scheduler.every(0.05, tick)
    scheduler.start()
    time.sleep(0.2)
    scheduler.stop()
    print("fired:", fired)
    assert "once" in fired
    assert fired.count("tick") >= 2


if __name__ == "__main__":
    main()
