import _thread
import time

def print_name(name, *arg):
    print(name, *arg)

name="Multithreading tutorial"
_thread.start_new_thread(print_name, (name, 1))
_thread.start_new_thread(print_name, (name, 1, 2))

time.sleep(0.5)
