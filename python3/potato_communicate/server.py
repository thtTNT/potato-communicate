import socket
from potato_communicate.client import Client as PCClient
import _thread


class Server:
    def __init__(self, port):
        self.server = socket.socket()
        self.server.bind(("0.0.0.0", port))
        self.server.listen(5)
        self.executor = lambda data: {}

    def listen(self):
        while True:
            client, address = self.server.accept()
            PCClient.fromSocket(client).whenData(lambda data: self.executor(data))

    def onMessage(self, executor):
        self.executor = executor
