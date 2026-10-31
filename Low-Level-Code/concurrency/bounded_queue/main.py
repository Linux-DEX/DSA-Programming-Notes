import threading

from bounded_queue import BoundedBlockingQueue


def main():
    queue = BoundedBlockingQueue(capacity=1)
    seen = []
    second_blocked = threading.Event()
    release_consumer = threading.Event()

    def producer():
        queue.put("a")
        second_blocked.set()
        queue.put("b")

    def consumer():
        second_blocked.wait()
        release_consumer.wait()
        seen.append(queue.get())
        seen.append(queue.get())

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    producer_thread.start()
    second_blocked.wait()
    assert seen == []
    release_consumer.set()
    producer_thread.join()
    consumer_thread.join()
    print("consumed:", seen)
    assert seen == ["a", "b"]


if __name__ == "__main__":
    main()
