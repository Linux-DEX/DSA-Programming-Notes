"""
Thread Synchronization in Python
---------------------------------
Demonstrates:
1. Synchronization using Locks
2. Synchronization using Condition variables
3. Synchronization using join() method
"""

import threading
import time

# ------------------------------
# 1. Synchronization Using Locks
# ------------------------------

print("=== Synchronization Using Locks ===")

counter = 10

def increment(lock, N):
    global counter
    for _ in range(N):
        lock.acquire()
        counter += 1
        lock.release()

lock = threading.Lock()

t1 = threading.Thread(target=increment, args=(lock, 2))
t2 = threading.Thread(target=increment, args=(lock, 10))
t3 = threading.Thread(target=increment, args=(lock, 4))

t1.start()
t2.start()
t3.start()

for t in (t1, t2, t3):
    t.join()

print("All threads have completed.")
print("The Final Counter Value:", counter)
print("\n")


# -----------------------------------------
# 2. Synchronization Using Condition Objects
# -----------------------------------------

print("=== Synchronization Using Condition Variables ===")

counter = 0

def consumer(cv):
    global counter
    with cv:
        print("Consumer is waiting")
        cv.wait()  # Wait until notified
        print("Consumer has been notified. Current Counter value:", counter)

def increment_with_condition(cv, N):
    global counter
    with cv:
        print("Increment is producing items")
        for i in range(1, N + 1):
            counter += i
        cv.notify()  # Notify consumer
        print("Increment has finished")

cv = threading.Condition()

consumer_thread = threading.Thread(target=consumer, args=(cv,))
increment_thread = threading.Thread(target=increment_with_condition, args=(cv, 5))

consumer_thread.start()
increment_thread.start()

consumer_thread.join()
increment_thread.join()

print("The Final Counter Value:", counter)
print("\n")


# -------------------------------------
# 3. Synchronization Using join() Method
# -------------------------------------

print("=== Synchronization Using join() Method ===")

class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Starting {self.name}")
        self.print_time(self.delay, 3)
        print(f"Exiting {self.name}")

    def print_time(self, delay, count):
        while count:
            time.sleep(delay)
            print(f"{self.name}: {time.ctime(time.time())}")
            count -= 1

# Create threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Exiting Main Thread")

