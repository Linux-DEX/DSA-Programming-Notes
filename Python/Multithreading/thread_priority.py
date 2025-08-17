"""
Thread Priority in Python
--------------------------
This script demonstrates:
1. Simulating thread priority using sleep delays
2. Setting real thread priority on Windows using ctypes
"""

import threading
import time
import ctypes
import platform

# ===================================================
# 1. Simulating Thread Priority Using time.sleep()
# ===================================================

print("== [1] Simulated Thread Priority with Sleep ==\n")

class DummyThread(threading.Thread):
    def __init__(self, name, priority):
        super().__init__()
        self.name = name
        self.priority = priority

    def run(self):
        # Higher priority = lower sleep = runs earlier
        time.sleep(1.0 * self.priority)
        print(f"{self.name} thread with priority {self.priority} is running")

# Create threads with simulated priority
t1 = DummyThread(name='Thread-1', priority=4)  # Lower priority (sleeps longer)
t2 = DummyThread(name='Thread-2', priority=1)  # Higher priority (sleeps less)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("All simulated-priority threads executed.\n")


# ===================================================
# 2. Adjusting Real Thread Priority on Windows
# ===================================================

print("== [2] Real Thread Priority (Windows Only) ==\n")

# Skip this section if not on Windows
if platform.system() == "Windows":
    # Constants for Windows API
    w32 = ctypes.windll.kernel32
    SET_THREAD = 0x20
    HIGH_PRIORITY = 1  # THREAD_PRIORITY_ABOVE_NORMAL or use proper enum

    class MyThread(threading.Thread):
        def __init__(self, start_event, name, iterations):
            super().__init__()
            self.start_event = start_event
            self.thread_id = None
            self.iterations = iterations
            self.name = name

        def set_priority(self, priority):
            if not self.is_alive():
                print(f"[{self.name}] Cannot set priority: thread not active.")
                return

            thread_handle = w32.OpenThread(SET_THREAD, False, self.thread_id)
            success = w32.SetThreadPriority(thread_handle, priority)
            w32.CloseHandle(thread_handle)

            if not success:
                print(f"[{self.name}] Failed to set priority. Error:", w32.GetLastError())
            else:
                print(f"[{self.name}] Priority set to {priority}")

        def run(self):
            self.thread_id = w32.GetCurrentThreadId()
            self.start_event.wait()
            for _ in range(self.iterations):
                print(f"[{self.name}] running...")
                start_time = time.time()
                while time.time() - start_time < 1:
                    pass

    # Create synchronization event
    start_event = threading.Event()

    # Create threads
    thread_normal = MyThread(start_event, name='Thread-Normal', iterations=4)
    thread_high = MyThread(start_event, name='Thread-High', iterations=4)

    # Start threads
    thread_normal.start()
    thread_high.start()

    # Set high priority (only after thread is alive)
    thread_high.set_priority(HIGH_PRIORITY)

    # Trigger both threads to start running
    start_event.set()

    # Wait for completion
    thread_normal.join()
    thread_high.join()

    print("All Windows-priority threads executed.\n")
else:
    print("Skipping Windows thread priority section: Not running on Windows.\n")

