"""
Thread Pooling in Python
-------------------------
Demonstrating:
1. ThreadPool using multiprocessing.dummy
2. ThreadPoolExecutor using concurrent.futures
"""

# ===================================================
# 1. Using Python ThreadPool Class (multiprocessing.dummy)
# ===================================================

from multiprocessing.dummy import Pool as ThreadPool
import time

def square(number):
    sqr = number * number
    time.sleep(1)
    print(f"[ThreadPool] Number: {number} | Square: {sqr}")

def cube(number):
    cub = number * number * number
    time.sleep(1)
    print(f"[ThreadPool] Number: {number} | Cube: {cub}")

print("== [1] ThreadPool with multiprocessing.dummy ==")

numbers = [1, 2, 3, 4, 5]

# Create a thread pool with 3 threads
pool = ThreadPool(3)

# Execute square and cube functions using map
pool.map(square, numbers)
pool.map(cube, numbers)

# Close the pool
pool.close()

print("== [1] ThreadPool Section Complete ==\n")


# ===================================================
# 2. Using Python ThreadPoolExecutor (concurrent.futures)
# ===================================================

from concurrent.futures import ThreadPoolExecutor
from time import sleep

def square(numbers):
    for val in numbers:
        ret = val * val
        sleep(1)
        print(f"[ThreadPoolExecutor] Number: {val} | Square: {ret}")

def cube(numbers):
    for val in numbers:
        ret = val * val * val
        sleep(1)
        print(f"[ThreadPoolExecutor] Number: {val} | Cube: {ret}")

print("== [2] ThreadPoolExecutor with concurrent.futures ==")

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create ThreadPoolExecutor with 4 threads
    executor = ThreadPoolExecutor(max_workers=4)

    # Submit tasks to the thread pool
    thread1 = executor.submit(square, numbers)
    thread2 = executor.submit(cube, numbers)

    # Check execution status
    print("Thread 1 executed? :", thread1.done())
    print("Thread 2 executed? :", thread2.done())

    # Wait for threads to complete
    sleep(2)

    # Check status again
    print("Thread 1 executed? :", thread1.done())
    print("Thread 2 executed? :", thread2.done())

    # Optionally wait for all tasks to complete before ending
    thread1.result()
    thread2.result()

    print("== [2] ThreadPoolExecutor Section Complete ==")

