import threading
import logging
import socket

socket_lock = threading.RLock()
client_lock = threading.RLock()

class ClientServer(Thread):

    def __init__ (self, port, host, max_device_count, in_queue, out_queue):
        client_lock.acquire()
        self.max_device_count = max_device_count
        self.connections = []
        client_lock.release()

        socket_lock.acquire()
        self.port = port
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpSocket.bind((host, port))
        socket_lock.release()

        self.listenThread = threading.Thread(target = self.listen_for_devices)
        self.listenThread.start()

    def listen_for_devices(self):
        max_devices_reached = False
        client_lock.acquire()
        if len(self.connections) != self.max_device_count:
            max_devices_reached = False
        else:
            True
        client_lock.release()

        socket_lock.acquire()
        self.tcpSocket.listen(1)
        while True:
            pair = self.tcpSocket.accept()
            sock, addr = pair
            print("Connected: %s" % repr(addr))
            client_lock.acquire()
            self.connections.append(sock)
            client_lock.release()
        socket_lock.release()

    def process_queue(self):
        queue_size = 0
        return queue_size
class Client:
    def __init__(self):
        return