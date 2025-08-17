"""
Main Thread Behavior in Python
------------------------------
Demonstrating:
1. Accessing main thread using threading
2. Differentiating main vs child thread
3. Parallel execution of main and child threads
4. Main thread waiting for other threads to finish
"""

import threading
import time
from threading import Thread
from time import sleep


# ===================================================
# 1. Accessing the Main Thread and Current Thread
# ===================================================

print("== [1] Accessing Main Thread ==")

name = 'Tutorialspoint'
print('Output:', name)
print('Current Thread:', threading.current_thread())

print()  # Line break


# ===================================================
# 2. Check if Current Thread is Main Thread
# ===================================================

print("== [2] Checking Main Thread ==")

def check_main_thread(x):
    time.sleep(x)
    if threading.current_thread() is not threading.main_thread():
        print('[Thread] Not running in the main thread.')

t = threading.Thread(target=check_main_thread, args=(0.5,))
t.start()

print('Main Thread:', threading.main_thread())
print("Main thread finished (without waiting for the worker thread)\n")

t.join()  # Ensure the thread finishes before moving on


# ===================================================
# 3. Main Thread Running Concurrently with Child Thread
# ===================================================

print("== [3] Concurrent Execution ==")

def worker_task(x):
    print('[Worker] Current Thread:', threading.current_thread())
    for n in range(x):
        print(f'[Worker] Running: {n}')
        time.sleep(0.3)
    print('[Worker] Finished...')

# Start a worker thread
worker = threading.Thread(target=worker_task, args=(6,))
worker.start()

# Main thread doing its own task
for i in range(3):
    print('[Main] Running:', i)
    time.sleep(0.5)

print("[Main] Main Thread Finished...\n")

worker.join()  # Wait for worker to finish before next section


# ===================================================
# 4. Main Thread Waiting for Other Threads
# ===================================================

print("== [4] Main Thread Waiting ==")

def my_function_1():
    print("[Worker 1] Started")
    sleep(1)
    print("[Worker 1] Done")

def my_function_2(thread_to_wait_for):
    print("[Worker 2] Waiting for Worker 1 to finish...")
    thread_to_wait_for.join()
    print("[Worker 2] Started after Worker 1")
    sleep(1)
    print("[Worker 2] Done")

# Create threads
worker1 = Thread(target=my_function_1)
worker2 = Thread(target=my_function_2, args=(worker1,))

# Start threads
worker1.start()
worker2.start()

# Main thread continues doing some work
for num in range(6):
    print(f"[Main] Main thread is working on task {num}")
    sleep(0.6)

# Ensure all threads finish
worker1.join()
worker2.join()

print("[Main] Main Thread Completed")

