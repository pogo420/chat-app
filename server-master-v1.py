import socket
import sys
from  multiprocessing import Process
import json


class ServerMaster:

    def __init__(self, port, host):
        self.port = port
        self.host = host


    def authenticate(self, user_id, access_key):
        '''Method for authentication'''
        db = None
        with open("chat-db.json") as f:
            db = json.load(f).get("access_key")
        if db.get(user_id) == access_key:
            return True
        return False


    def db_connect(self, to, frm, message):
        '''Method for db connect'''
        pass


    def command_parse(self,s):
        '''Method for command parsing
        input format: {
            "user_id": "1235",
            "access_key": "access_key",
            "message": "message",
            "to": "1238",
            "request_dt": '%Y-%m-%d-%H:%M:%S'
        }
        '''
        client_request = json.loads(s)
        user_id = client_request.get("user_id")
        access_key = client_request.get("access_key")
        if not self.authenticate(user_id, access_key):
            print("authentication error")
            sys.exit(0)
        return (
        client_request.get("to"),
        client_request.get("user_id"),
        client_request.get("message")
        )


    def main(self):
        '''Main method'''
        with socket.socket() as sk:
            sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reusing port
            sk.bind((self.host, self.port)) # bind
            sk.listen(5) # listen
            conn, addrs = sk.accept() # accept
            print("serving client:",addrs)
            client_request = conn.recv(1024) # data from client
            to, frm, client_message = self.command_parse(client_request) # command parsing + authentication
            print("data received", client_message)

            conn.close()
            sk.close()


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8001
    while True:
        p = Process(ServerMaster(PORT,HOST).main())
        p.start()
        p.join()
