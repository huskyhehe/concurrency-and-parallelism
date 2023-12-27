import multiprocessing
import random
from multiprocessing import Process, Queue, current_process


def child_process(q: Queue) -> None:
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
    4
    0
    5
    9
    7
    0
    6
    9
    5
    8
    5
    3
    5
    7
    8
    2
    2
    6
    0
    3
    7
    5
    3
    2
    9
    6
    1
    4
    6
    7
    9
    5
    3
    2
    4
    4
    5
    5
    3
    0
    1
    3
    3
    1
    9
    3
    2
    3
    8
    4
    6
    2
    9
    0
    6
    4
    2
    2
    8
    6
    2
    6
    0
    0
    5
    4
    7
    7
    0
    4
    3
    1
    6
    7
    3
    7
    3
    3
    0
    2
    9
    7
    8
    4
    1
    9
    6
    51
    
    7
    5
    5
    4
    2
    8
    3
    9
    3
    6
    6
    child process Process-2 processed 24 items from the queue
    child process Process-1 processed 76 items from the queue
    '''
