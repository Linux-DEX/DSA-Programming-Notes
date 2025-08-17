"""
Naming Threads in Python
-------------------------
This script demonstrates:
1. Assigning names at thread creation
2. Dynamically renaming threads during execution
3. Using thread names in multi-threaded functions
"""

import threading
from time import sleep

# --------------------------------------------
# Part 1: Naming Threads at Creation
# --------------------------------------------

def show_thread_name_1(arg):
    print("This thread's name is:", threading.current_thread().name)

# Creating threads with and without custom names
thread1 = threading.Thread(target=show_thread_name_1, name='My_Thread_1', args=(2,))
thread2 = threading.Thread(target=show_thread_name_1, args=(3,))  # Defaults to Thread-N

print("\n[Main] Current thread's name is:", threading.current_thread().name)

# Start and join threads
thread1.start()
thread1.join()

thread2.start()
thread2.join()


# --------------------------------------------
# Part 2: Dynamically Renaming Threads at Runtime
# --------------------------------------------

def show_thread_name_2(arg):
    # Rename the current thread dynamically
    threading.current_thread().name = "Dynamic_Name"
    print("This thread's name is (after rename):", threading.current_thread().name)

# Create threads (one named, one default)
thread3 = threading.Thread(target=show_thread_name_2, name='Initially_Named', args=(2,))
thread4 = threading.Thread(target=show_thread_name_2, args=(3,))

print("\n[Main] Current thread's name is:", threading.current_thread().name)

# Start and join threads
thread3.start()
thread3.join()

thread4.start()
thread4.join()


# --------------------------------------------
# Part 3: Using Custom Thread Names in Function Logic
# --------------------------------------------

def addition_of_numbers(x, y):
    print("This thread's name is:", threading.current_thread().name)
    result = x + y
    print(f"Addition Result: {x} + {y} = {result}")

def cube_number(i):
    print("This thread's name is:", threading.current_thread().name)
    result = i ** 3
    print(f"Cube Result: {i}^3 = {result}")

def basic_function():
    print("This thread's name is:", threading.current_thread().name)
    print("Basic function running...")

# Create threads with and without custom names
t1 = threading.Thread(target=addition_of_numbers, name='Addition_Thread', args=(2, 4))
t2 = threading.Thread(target=cube_number, args=(4,))  # Will get default name
t3 = threading.Thread(target=basic_function)          # Will assign name later

# Start and join threads
t1.start()
t1.join()

t2.start()
t2.join()

# Assign name dynamically before starting
t3.name = 'Custom_Basic_Function_Thread'
t3.start()
t3.join()

# Final statement from main thread
print("\n[Main] Current thread's name is:", threading.current_thread().name)

