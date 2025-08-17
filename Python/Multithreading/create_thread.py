"""
Threading Examples in Python
----------------------------
Demonstrating:
1. Creating threads using functions
2. Creating threads by extending the Thread class
3. Creating threads using _thread.start_new_thread()
"""

import threading
import time
import _thread

# ------------------------------
# 1. Creating Threads with Functions
# ------------------------------

def addition_of_numbers(x, y):
    result = x + y
    print(f'Addition of {x} + {y} = {result}')

def cube_number(i):
    result = i ** 3
    print(f'Cube of {i} = {result}')

def basic_function():
    print("Basic function is running concurrently...")

# Start threads using functions
threading.Thread(target=addition_of_numbers, args=(2, 4)).start()
threading.Thread(target=cube_number, args=(4,)).start()
threading.Thread(target=basic_function).start()

# ------------------------------
# 2. Creating Threads by Extending the Thread Class
# ------------------------------

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Starting {self.name}")
        self.print_time(5, self.delay)
        print(f"Exiting {self.name}")

    def print_time(self, counter, delay):
        while counter:
            if exitFlag:
                break
            time.sleep(delay)
            print(f"{self.name}: {time.ctime(time.time())}")
            counter -= 1

# Create and start threads using class extension
thread1 = MyThread(1, "Thread-Class-1", 1)
thread2 = MyThread(2, "Thread-Class-2", 2)

thread1.start()
thread2.start()

# ------------------------------
# 3. Creating Threads using _thread.start_new_thread()
# ------------------------------

def thread_task(threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print(f"Thread name: {threadName} Count: {count}")

# Create threads using low-level _thread module
try:
    _thread.start_new_thread(thread_task, ("LowLevel-Thread-1", 2))
    _thread.start_new_thread(thread_task, ("LowLevel-Thread-2", 4))
except:
    print("Error: unable to start thread")

# ------------------------------
# Wait for threads to complete
# ------------------------------

# Join threads created using threading.Thread and subclass
thread1.join()
thread2.join()

# Prevent main thread from exiting immediately (for low-level threads)
# It's better than using `while True: pass`
time.sleep(10)

print("Exiting Main Thread")

