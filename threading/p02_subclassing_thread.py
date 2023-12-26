from threading import Thread, current_thread


class MyTask(Thread):
    def __init__(self):
        Thread.__init__(self, name="subclassThread", args=(2, 3))

    def run(self):
        print(f"{current_thread().name} is executing")


if __name__ == "__main__":
    myTask = MyTask()
    myTask.start()
    myTask.join()
    myTask.run()

    '''
    subclassThread is executing
    MainThread is executing
    '''

