from threading import Thread, current_thread


def thread_task(a, b, c, key1, key2):
    print(f"{current_thread().name} received the arguments: {a}, {b}, {c}, {key1}, {key2}")


if __name__ == "__main__":
    myThread = Thread(group=None,
                      target=thread_task,
                      args=(1, 2, 3),
                      name="demoThread",
                      kwargs={'key1': 777, 'key2': 111},
                      daemon=None
                      )

    myThread.start()
    myThread.join()

    '''
    demoThread received the arguments: 1, 2, 3, 777, 111
    '''