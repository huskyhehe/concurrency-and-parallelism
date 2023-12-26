import time
from threading import Lock, Thread, current_thread

shared_state = [1, 2, 3]
my_lock = Lock()


def thread1_operations():
    my_lock.acquire()
    print(f"{current_thread().name} has acquired the lock")

    time.sleep(3)
    shared_state[0] = 777

    print(f"{current_thread().name} is about to release the lock")
    my_lock.release()
    print(f"{current_thread().name} has released the lock")


def thread2_operations():
    print(f"{current_thread().name} is attempting to acquire the lock")
    my_lock.acquire()
    print(f"{current_thread().name} has acquired the lock")

    print(shared_state[0])
    print(f"{current_thread().name} is about to release the lock")
    my_lock.release()
    print(f"{current_thread().name} has released the lock")


if __name__ == "__main__":
    # create and run the two threads
    thread1 = Thread(target=thread1_operations, name="thread1")
    thread1.start()

    thread2 = Thread(target=thread2_operations, name="thread2")
    thread2.start()

    # wait for the two threads to complete
    thread1.join()
    thread2.join()

    '''
    thread1 has acquired the lock
    thread2 is attempting to acquire the lock
    thread1 is about to release the lock
    thread1 has released the lock
    thread2 has acquired the lock
    777
    thread2 is about to release the lock
    thread2 has released the lock
    '''
