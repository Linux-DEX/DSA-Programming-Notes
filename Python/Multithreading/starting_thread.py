"""
Starting Threads in Python
---------------------------
1. Using threading.Thread with a target function
2. By creating a custom thread class (extending Thread)
"""

from threading import Thread
from time import sleep
import threading
import time

# --------------------------------------------
# Part 1: Using threading.Thread with a function
# --------------------------------------------

def my_function(arg):
    """Function executed by a basic thread"""
    for i in range(arg):
        print(f"Child Thread running {i}")
        sleep(0.5)

# Create and start the thread
basic_thread = Thread(target=my_function, args=(10,))
basic_thread.start()

print("Main thread continues after starting basic_thread...\n")

# --------------------------------------------
# Part 2: Using a custom thread class
# --------------------------------------------

class MyThread(threading.Thread):
    """Custom thread class extending threading.Thread"""
    def __init__(self, threadID, name, counter):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}")
        self.print_time(self.counter)
        print(f"Exiting {self.name}\n")

    def print_time(self, counter):
        while counter:
            time.sleep(1)
            print(f"{self.name}: {time.ctime(time.time())}")
            counter -= 1

# Create instances of MyThread
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
thread3 = MyThread(3, "Thread-3", 3)

# Start only thread1 and thread3
thread1.start()
thread3.start()

# Optionally: wait for all threads to finish
basic_thread.join()
thread1.join()
thread3.join()

print("Main Thread Exiting")

