import multiprocessing
import random
from multiprocessing import Process, Queue, current_process


def child_process(q):
    count = 0
    while not q.empty():
        try:
            print(q.get(block=False, timeout=5))
            count += 1
        except:
            pass

        # we enclose the get method in a try-except block
        # because an empty queue raises an empty queue exception
        # when using the non-blocking version of the get call.

    print(f"child process {current_process().name} processed {count} items from the queue", flush=True)


if __name__ == '__main__':
    # multiprocessing.set_start_method("fork")
    q = Queue()

    print(f"This machine has {multiprocessing.cpu_count()} CPUs")
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    '''
    This machine has 8 CPUs
    9
    2
    3
    9
    5
    6
    7
    8
    5
    8
    4
    0
    3
    0
    3
    5
    8
    1
    3
    5
    6
    9
    3
    0
    8
    6
    4
    5
    3
    0
    6
    6
    3
    4
    3
    0
    7
    3
    5
    6
    2
    6
    6
    3
    3
    3
    0
    5
    4
    7
    5
    9
    6
    5
    5
    3
    1
    9
    2
    5
    9
    1
    7
    9
    6
    8
    2
    4
    3
    0
    6
    5
    3
    0
    9
    2
    6
    2
    4
    9
    9
    0
    6
    1
    1
    2
    6
    1
    2
    3
    1
    9
    3
    8
    4
    8
    7
    9
    2
    1
    child process Process-1 processed 61 items from the queue
    child process Process-2 processed 39 items from the queue
    '''
