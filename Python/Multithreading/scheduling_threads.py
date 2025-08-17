"""
Scheduling Threads and Tasks in Python
--------------------------------------
This script demonstrates:
1. Scheduling with threading.Timer
2. Scheduling with sched.scheduler
3. Scheduling a function with arguments using sched
"""

import threading
import sched
import time
from datetime import datetime


# ===================================================
# 1. Scheduling Threads using threading.Timer
# ===================================================

def schedule_event_thread(name, start):
    now = time.time()
    elapsed = int(now - start)
    print(f'[threading.Timer] Elapsed: {elapsed} seconds | Name: {name}')

# Record start time
start_timer = time.time()
print('\n== [1] THREADING.TIMER START ==')
print('START:', time.ctime(start_timer))

# Schedule events
t1 = threading.Timer(3, schedule_event_thread, args=('EVENT_1', start_timer))
t2 = threading.Timer(2, schedule_event_thread, args=('EVENT_2', start_timer))

# Start timers
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

# Record end time
end_timer = time.time()
print('END:', time.ctime(end_timer))
print('== [1] THREADING.TIMER END ==\n')


# ===================================================
# 2. Scheduling Events using sched.scheduler
# ===================================================

def schedule_event_sched(name, start):
    now = time.time()
    elapsed = int(now - start)
    print(f'[sched.scheduler] Elapsed: {elapsed} seconds | Name: {name}')

# Create scheduler instance
scheduler = sched.scheduler(time.time, time.sleep)

# Record start time
start_sched = time.time()
print('== [2] SCHED.SCHEDULER START ==')
print('START:', time.ctime(start_sched))

# Schedule events
scheduler.enter(2, 1, schedule_event_sched, argument=('EVENT_1', start_sched))
scheduler.enter(5, 1, schedule_event_sched, argument=('EVENT_2', start_sched))

# Run scheduled tasks
scheduler.run()

# Record end time
end_sched = time.time()
print('END:', time.ctime(end_sched))
print('== [2] SCHED.SCHEDULER END ==\n')


# ===================================================
# 3. Scheduling Function with Arguments using sched
# ===================================================

def addition(a, b):
    print("\n[sched.scheduler with args] Performing Addition")
    print("Current Time:", datetime.now())
    print("Monotonic Time:", time.monotonic())
    print(f"Result: {a} + {b} = {a + b}")

# Create scheduler instance
s = sched.scheduler(time.time, time.sleep)

# Record start time
print('== [3] SCHED WITH ARGUMENTS START ==')
print('START TIME:', datetime.now())

# Schedule the addition function
event1 = s.enter(4, 1, addition, argument=(5, 6))
print("Event Scheduled:", event1)

# Run the scheduled function
s.run()

# Record end time
print('END TIME:', datetime.now())
print('== [3] SCHED WITH ARGUMENTS END ==')

