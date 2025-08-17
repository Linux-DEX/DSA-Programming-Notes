# Multithreading

- Multithreading allows you to run multiple threads concurrently within a single process, which is also known as thread-based parallelis.
- This means a program can perform multiple tasks at the same time, enhancing its efficiency and responsiveness.
- Multithreading in Python is especially useful for multiple I/O-bound operations, rather than for tasks that require heavy computation.

[Multithreading note](https://www.tutorialspoint.com/python/python_multithreading.htm)

---

# Python Thread Handling Modules

Python's standard library provides two main modules for managing threads: `_thread` and `threading`.

---

## `_thread` Module (Low-Level Threading)

The `_thread` module provides basic APIs to manage threads and simple locks (mutexes).  
It is suitable for simple, low-level use cases.

### Example: `_thread` Module
See: [`_thread_example.py`](./_thread_example.py)

---

## `threading` Module (High-Level Threading)

Introduced in Python 2.4, the `threading` module builds on `_thread`, providing more powerful and flexible threading support.

### Key Features:

- `threading.activeCount()`: Returns the number of active threads.
- `threading.currentThread()`: Returns the current thread object.
- `threading.enumerate()`: Returns a list of all active threads.

### Thread Class Methods:

| Method       | Description                                   |
|--------------|-----------------------------------------------|
| `start()`    | Starts the thread.                            |
| `run()`      | Entry point for the thread.                   |
| `join()`     | Waits for the thread to finish.               |
| `isAlive()`  | Checks if the thread is still running.        |
| `getName()`  | Gets the thread’s name.                       |
| `setName()`  | Sets the thread’s name.                       |

---

## Example: Basic Threading

Uses the `threading.Thread` class to create and run threads.  
See: [`threading_example.py`](./threading_example.py)

---

## Synchronizing Threads

To avoid race conditions, use `threading.Lock()`.

### Example:
- Acquire a lock before accessing shared resources.
- Release it afterward.

See: [`sync_threads.py`](./sync_threads.py)

---

## Multithreaded Priority Queue

The `queue` module can be used for safe sharing of data between threads.

### Key Queue Methods:

| Method     | Description                             |
|------------|-----------------------------------------|
| `get()`    | Removes and returns an item from queue. |
| `put()`    | Adds item to queue.                     |
| `qsize()`  | Returns queue size.                     |
| `empty()`  | Checks if queue is empty.               |
| `full()`   | Checks if queue is full.                |

### Example:  
See: [`priority_queue.py`](./priority_queue.py)

---

## **Thread Life cycle**

A thread object goes through different stages during its life cycle. When a new thread object is created, it must be started, which calls the run() method of thread class. This method contains the logic of the process to be performed by the new thread. The thread completes its task as the run() method is over, and the newly created thread merges with the main thread.

While a thread is running, it may be paused either for a predefined duration or it may be asked to pause till a certain event occurs. The thread resumes after the specified interval or the process is over.

### States of a Thread Life Cycle in Python

> [!NOTE]
> - Creating a Thread − To create a new thread in Python, you typically use the Thread class from the threading module.
> - Starting a Thread − Once a thread object is created, it must be started by calling its start() method. This initiates the thread's activity and invokes its run() method in a separate thread.
> - Paused/Blocked State − Threads can be paused or blocked for various reasons, such as waiting for I/O operations to complete or another thread to perform a task. This is typically managed by calling its join() method. This blocks the calling thread until the thread being joined terminates.
> - Synchronizing Threads − Synchronization ensures orderly execution and shared resource management among threads. This can be done by using synchronization primitives like locks, semaphores, or condition variables.
> - Termination − A thread terminates when its run() method completes execution, either by finishing its task or encountering an exception.

