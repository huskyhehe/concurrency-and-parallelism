from threading import Thread, current_thread
import time


def regular_thread_task():
    while True:
        print(f"{current_thread().name} executing")
        time.sleep(1)


def with_daemon():
    print("with daemon:")
    regular_thread = Thread(target=regular_thread_task, name="regular_thread", daemon=True)
    regular_thread.start()  # start the regular thread

    time.sleep(3)

    print("Main thread exiting but Python program doesn't")

    '''
    with daemon:
    regular_thread executing
    regular_thread executing
    regular_thread executing
    Main thread exiting but Python program doesn't
    '''


def without_daemon():
    print("without daemon:")
    regular_thread = Thread(target=regular_thread_task, name="regular_thread", daemon=False)
    regular_thread.start()  # start the regular thread

    time.sleep(3)

    print("Main thread exiting but Python program doesn't")

    '''
    without daemon:
    regular_thread executing
    regular_thread executing
    regular_thread executing
    regular_thread executing
    regular_thread executing
    regular_thread executing
    Main thread exiting but Python program doesn't
    regular_thread executing
    regular_thread executing
    regular_thread executing
    regular_thread executing
    ...
    '''


if __name__ == "__main__":
    with_daemon()
    without_daemon()
