from multiprocessing import Process, Pipe
import time


def child_process(conn: Pipe) -> None:
    for i in range(10):
        conn.send("hello " + str(i))
    conn.close()


if __name__ == '__main__':
    # Using pipes for interprocess communication

    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    time.sleep(3)

    for _ in range(10):
        msg = parent_conn.recv()
        print(msg)

    parent_conn.close()
    p.join()
