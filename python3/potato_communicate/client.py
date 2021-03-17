import socket
import potato_communicate.converter as converter
import threading


class Receiver(threading.Thread):
    def __init__(self, conn, callback):
        threading.Thread.__init__(self)
        self.conn = conn
        self.callback = callback

    def run(self):
        tmp = ""
        while True:
            data = self.conn.recv(1024)
            for char in data:
                if char == 10:
                    self.callback(converter.fromPCO(tmp))
                    tmp = ""
                else:
                    tmp += chr(char)


class Client:

    @staticmethod
    def connect(ip, port):
        conn = socket.socket()
        conn.connect((ip, port))
        client = Client(conn)
        return client

    @staticmethod
    def fromSocket(conn):
        client = Client(conn)
        return client

    def onData(self, data):
        self.dataEvent(data)

    def __init__(self, conn):
        self.conn = conn
        self.dataEvent = lambda data: {}
        Receiver(conn, lambda data: self.onData(data)).start()

    def write(self, obj):
        self.conn.send(converter.toPCO(obj) + "\n")

    def whenData(self, executor):
        self.dataEvent = executor


