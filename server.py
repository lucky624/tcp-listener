import socket, uuid
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(c):
    while True:
        data = c.recv(2048)
        if data:
            handle = open('data/' + "output_" + uuid.uuid4().hex, 'wb')
            handle.write(data)
            handle.close()
        if not data:
            print_lock.release()
            break
        print(data)
    c.close()


def Main():
    host = "0.0.0.0"
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        print_lock.acquire()
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main() 