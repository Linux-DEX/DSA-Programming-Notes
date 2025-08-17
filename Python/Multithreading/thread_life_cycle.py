"""
Python Thread Life Cycle Demonstration
--------------------------------------
1. Demonstrating thread creation, running, and termination
2. Demonstrating synchronization using Semaphore
"""

import threading
import time

# --------------------------------------------
# Part 1: Thread Life Cycle
# --------------------------------------------

def thread_task(x):
    """Function to simulate thread activity"""
    print(f'Current Thread Details: {threading.current_thread()}')
    for n in range(x):
        print(f'{threading.current_thread().name} Running {n}')
    print(f'{threading.current_thread().name} Finished Execution\n')

# Create threads (Thread state: CREATED)
t1 = threading.Thread(target=thread_task, args=(2,), name='Worker-1')
t2 = threading.Thread(target=thread_task, args=(3,), name='Worker-2')

print('--- Thread State: CREATED ---')

# Start the threads (Thread state: RUNNING)
t1.start()
t2.start()

# Wait for threads to finish (Thread state: TERMINATED after join)
t1.join()
t2.join()

print('--- Thread State: FINISHED ---')

# Simulate main thread work
for i in range(3):
    print(f'Main Thread Running {i}')

print("Main Thread Finished\n")

# --------------------------------------------
# Part 2: Using a Synchronization Primitive (Semaphore)
# --------------------------------------------

# A semaphore that allows only 2 threads to run concurrently
semaphore = threading.Semaphore(2)

def worker_with_semaphore():
    """Worker function with semaphore-controlled access"""
    with semaphore:
        print(f'{threading.current_thread().name} has started working')
        time.sleep(2)
        print(f'{threading.current_thread().name} has finished working')

# Create and start multiple threads
sync_threads = []

print('--- Creating Threads with Semaphore Control ---')
for i in range(5):
    t = threading.Thread(target=worker_with_semaphore, name=f'Semaphore-Thread-{i+1}')
    sync_threads.append(t)
    print(f'{t.name} has been created')
    t.start()

# Wait for all threads to complete
for t in sync_threads:
    t.join()
    print(f'{t.name} has terminated')

print('--- All Semaphore Threads FINISHED ---')
print("Main Thread Finished")

