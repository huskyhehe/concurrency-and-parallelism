from multiprocessing import Process
from multiprocessing import current_process
import os


def process_task1():
    print(f"{current_process().name} has pid: {os.getpid()} with parent pid: {os.getppid()}")


def example1():
    process = [0] * 3

    for i in range(0, 3):
        process[i] = Process(target=process_task1, name="process-{0}".format(i))
        process[i].start()

    for i in range(0, 3):
        process[i].join()

    print(f"{current_process().name} has pid: {os.getpid()} ")

    '''
    process-0 has pid: 24532 with parent pid: 19688
    process-1 has pid: 13356 with parent pid: 19688
    process-2 has pid: 468 with parent pid: 19688
    MainProcess has pid: 19688 
    '''


def process_task2(x, y, z, key1, key2):
    print(f"{current_process().name} has pid: {os.getpid()} with parent pid: {os.getppid()}")
    print(f"Received arguments {x} {y} {z} {key1} {key2}")


def example2():
    process = Process(target=process_task2,
                      name="process-with-args",
                      args=(1, 2, 3),
                      kwargs={
                          'key1': 'arg1',
                          'key2': 'arg2'
                      })
    process.start()

    process.join()

    '''
    process-with-args has pid: 17992 with parent pid: 3816
    Received arguments 1 2 3 arg1 arg2
    '''


if __name__ == "__main__":
    example1()
    example2()
