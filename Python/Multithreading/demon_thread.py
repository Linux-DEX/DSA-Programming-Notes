"""
Daemon Threads in Python
-------------------------
This script demonstrates:
1. Creating a daemon thread using constructor
2. Setting the daemon attribute before start
3. Attempting to change daemon status after start (not allowed)
"""

import threading
from time import sleep


# ===================================================
# 1. Creating a Daemon Thread Using Constructor
# ===================================================

def run_daemon_param():
    thread = threading.current_thread()
    print(f"[run_daemon_param] Daemon thread? {thread.daemon}")

print("== [1] Daemon Thread via Constructor ==")

thread1 = threading.Thread(target=run_daemon_param, daemon=True)
thread1.start()

print("Main Thread Daemon? :", threading.current_thread().daemon)
sleep(0.5)  # Allow daemon thread to execute


# ===================================================
# 2. Setting daemon attribute BEFORE starting
# ===================================================

def run_daemon_property():
    thread = threading.current_thread()
    print(f"[run_daemon_property] Daemon thread? {thread.daemon}")

print("\n== [2] Setting daemon=True before start ==")

thread2 = threading.Thread(target=run_daemon_property)
thread2.daemon = True  # Set before starting
thread2.start()

print("Main Thread Daemon? :", threading.current_thread().daemon)
sleep(0.5)  # Allow daemon thread to execute


# ===================================================
# 3. Attempting to Set daemon AFTER Start (Incorrect)
# ===================================================

from threading import Thread, current_thread

def run_set_daemon_late():
    thread = current_thread()
    print(f"[run_set_daemon_late] Daemon thread? {thread.daemon}")
    
    try:
        # Attempt to set daemon after thread is running (this will fail)
        thread.daemon = True
    except RuntimeError as e:
        print(f"[run_set_daemon_late] Error: {e}")

print("\n== [3] Attempting to set daemon after thread starts ==")

thread3 = Thread(target=run_set_daemon_late)
thread3.start()

sleep(0.5)  # Give thread time to run

