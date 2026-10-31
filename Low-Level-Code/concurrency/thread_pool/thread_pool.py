import sys
import threading
import queue


class ThreadPool:
    """
    Fixed workers pulling tasks from a queue.

    submit(func, args) queues work. shutdown waits for queued tasks,
    then stops the workers.

    ponytail: the task queue is unbounded. Bound it with the
    BoundedBlockingQueue when producers must slow down.
    """

    def __init__(self, worker_count):
        if worker_count <= 0:
            raise ValueError("worker_count must be positive")
        self._tasks = queue.Queue()
        self._shutdown = False
        self._workers = []
        for index in range(worker_count):
            thread = threading.Thread(target=self._run, name=f"worker-{index}")
            thread.start()
            self._workers.append(thread)

    def submit(self, func, args):
        if self._shutdown:
            raise RuntimeError("pool shut down")
        self._tasks.put((func, args))

    def shutdown(self):
        self._shutdown = True
        for _ in self._workers:
            self._tasks.put((None, ()))
        for thread in self._workers:
            thread.join()

    def _run(self):
        while True:
            func, args = self._tasks.get()
            try:
                if func is None:
                    return
                func(*args)
            except Exception as exc:
                print(f"task failed: {exc}", file=sys.stderr)
            finally:
                self._tasks.task_done()
