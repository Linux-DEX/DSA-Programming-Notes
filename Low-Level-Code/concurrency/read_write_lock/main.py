import threading
import time

from read_write_lock import ReadWriteLock


def main():
    lock = ReadWriteLock()
    order = []
    reader_in = threading.Event()
    release_reader = threading.Event()
    writer_waiting = threading.Event()
    allow_second_reader = threading.Event()

    def reader():
        lock.acquire_read()
        order.append("read-start")
        reader_in.set()
        release_reader.wait()
        order.append("read-end")
        lock.release_read()

    def writer():
        reader_in.wait()
        order.append("write-wait")
        writer_waiting.set()
        lock.acquire_write()
        order.append("write-start")
        lock.release_write()

    def later_reader():
        allow_second_reader.wait()
        lock.acquire_read()
        order.append("read2")
        lock.release_read()

    threads = [
        threading.Thread(target=reader),
        threading.Thread(target=writer),
        threading.Thread(target=later_reader),
    ]
    for thread in threads:
        thread.start()

    writer_waiting.wait()
    while lock._waiting_writers == 0:
        time.sleep(0.001)
    allow_second_reader.set()
    time.sleep(0.05)
    assert "write-start" not in order
    assert "read2" not in order

    release_reader.set()
    for thread in threads:
        thread.join()

    print("order:", order)
    assert order.index("read-end") < order.index("write-start")
    assert order.index("write-start") < order.index("read2")


if __name__ == "__main__":
    main()
