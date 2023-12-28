from multiprocessing import Process, Queue, Semaphore
import multiprocessing


def child_process(q, sem1, sem2):
    var = q.get()
    print(f"Child process received var = {var} with id {id(var)} from queue")
    sem2.release()
    sem1.acquire()

    print(f"After changes by parent process var in child process = {var}", flush=True)


if __name__ == '__main__':
    q = Queue()
    # A Semaphore is a synchronization primitive in programming that is used
    # to control access to a shared resource by multiple processes or threads.
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print(f"This machine has {multiprocessing.cpu_count()} CPUs")

    n = {"key": "value"}
    print(f"Parent process puts item on queue with id {id(n)}")
    q.put(n)

    process = Process(target=child_process, args=(q, sem1, sem2))
    process.start()

    sem2.acquire()

    # change the dictionary object
    n["key"] = "new-value"
    print(f"Parent process changed the enqueued item to {n}", flush=True)
    sem1.release()
    process.join()

    '''
    This machine has 8 CPUs
    Parent process puts item on queue with id 2758285885632
    Child process received var = {'key': 'value'} with id 2975759641984 from queue
    Parent process changed the enqueued item to {'key': 'new-value'}
    After changes by parent process var in child process = {'key': 'value'}
    '''
