import threading
import time


class Scheduler:
    """
    Run a job once at a monotonic time, or every `interval` seconds.

    at(run_at, fn) runs once. every(interval, fn) runs first after one
    interval, then again after each successful run.

    ponytail: jobs are a list sorted on each wake. Use a heap when
    the schedule holds more than a handful of jobs.
    """

    def __init__(self):
        self._jobs = []
        self._cond = threading.Condition()
        self._running = False
        self._thread = None

    def at(self, run_at, fn):
        with self._cond:
            self._jobs.append([run_at, None, fn])
            self._cond.notify()

    def every(self, interval, fn):
        if interval <= 0:
            raise ValueError("interval must be positive")
        with self._cond:
            self._jobs.append([time.monotonic() + interval, interval, fn])
            self._cond.notify()

    def start(self):
        with self._cond:
            if self._running:
                return
            self._running = True
            self._thread = threading.Thread(target=self._loop)
            self._thread.start()

    def stop(self):
        with self._cond:
            self._running = False
            self._cond.notify_all()
        if self._thread is not None:
            self._thread.join()

    def _loop(self):
        while True:
            with self._cond:
                if not self._running:
                    return
                if not self._jobs:
                    self._cond.wait()
                    continue
                self._jobs.sort(key=lambda job: job[0])
                wait = self._jobs[0][0] - time.monotonic()
                if wait > 0:
                    self._cond.wait(timeout=wait)
                    continue
                job = self._jobs.pop(0)
            job[2]()
            interval = job[1]
            if interval is None:
                continue
            with self._cond:
                if not self._running:
                    return
                job[0] = time.monotonic() + interval
                self._jobs.append(job)
                self._cond.notify()
