"""
Joining Threads in Python
--------------------------
This script demonstrates:
1. Using join() to wait for threads to complete
2. Using join(timeout) to wait for a thread for a limited time
"""

from threading import Thread
from time import sleep

# --------------------------------------------
# Example 1: Using join() without timeout
# --------------------------------------------

def my_function_1(arg):
    for i in range(arg):
        print("Child Thread 1 running", i)
        sleep(0.5)

def my_function_2(arg):
    for i in range(arg):
        print("Child Thread 2 running", i)
        sleep(0.1)

# Create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_2, args=(3,))

print("\n--- Example 1: join() without timeout ---")

# Start thread1 and wait for it to complete
thread1.start()
thread1.join()  # Main thread waits until thread1 completes

# Start thread2 and wait for it to complete
thread2.start()
thread2.join()  # Main thread waits until thread2 completes

print("Main thread finished...exiting Example 1")

# --------------------------------------------
# Example 2: Using join() with timeout
# --------------------------------------------

# Re-create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_2, args=(3,))

print("\n--- Example 2: join() with timeout ---")

# Start thread1 and wait for 0.2 seconds only
thread1.start()
thread1.join(timeout=0.2)  # Main thread only waits briefly

# Start thread2 and wait for it to complete
thread2.start()
thread2.join()

# Optional: wait for thread1 to finish (if it hasn't already)
thread1.join()

print("Main thread finished...exiting Example 2")

