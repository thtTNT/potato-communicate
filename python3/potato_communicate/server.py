import socket
from potato_communicate.client import Client as PCClient
import _thread


class Server:
    def __init__(self, port):
        self.server = socket.socket()
        self.server.bind(("0.0.0.0", port))
        self.server.listen(5)
        self.events = {
            "client": lambda new_client: {}
        }

    def listen(self):
        while True:
            client, address = self.server.accept()
            self.events["client"](PCClient.fromSocket(client))

    def on(self, name, executor):
        self.events[name] = executor
