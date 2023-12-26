from threading import Thread, Lock
import time


def thread_one(lock1, lock2):
    lock1.acquire()
    time.sleep(1)
    lock2.release()


def thread_two(lock1, lock2):
    lock2.acquire()
    time.sleep(1)
    lock1.release()


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=thread_one, args=(lock1, lock2))
    t2 = Thread(target=thread_one, args=(lock1, lock2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    '''
    Exception in thread Thread-1 (thread_one):
    Traceback (most recent call last):
      File "D:\Program Files\Python311\Lib\threading.py", line 1038, in _bootstrap_inner
        self.run()
      File "D:\Program Files\Python311\Lib\threading.py", line 975, in run
        self._target(*self._args, **self._kwargs)
      File "D:\NEU\CSYE7105\concurrency-and-parallelism\threading\p2_04_deadlock.py", line 8, in thread_one
        lock2.release()
    RuntimeError: release unlocked lock
    '''