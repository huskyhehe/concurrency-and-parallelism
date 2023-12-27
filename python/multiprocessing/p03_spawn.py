from multiprocessing import Process
import multiprocessing

global_arg = "this is a global arg"


def process_task(garg, larg):
    print(garg + " - " + larg)


if __name__ == '__main__':

    multiprocessing.set_start_method('spawn')
    local_arg = "this is a global arg"

    process = Process(target=process_task, name="process-1", args=(global_arg, local_arg))
    process.start()
    process.join()

    '''
    this is a global arg - this is a global arg
    '''
