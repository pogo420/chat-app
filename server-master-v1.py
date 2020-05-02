import socket
import sys
from  multiprocessing import Process


class ServerMaster:
    
    def __init__(self, port, host):
        self.port = port
        self.host = host

    @staticmethod
    def transform(s):
        '''Method for some arbitary transform'''
        s = s.upper()
        return s

    def client_connect(self):
        with socket.socket() as sk:
            sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reusing port 
            sk.bind((self.host, self.port)) # bind
            sk.listen(5) # listen
            conn, addrs = sk.accept() # accept 
            print("serving client:",addrs) 
            data = conn.recv(1024) # data in
            print("data received", data)
            conn.close()
            sk.close()


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8001
    while True:
        p = Process(ServerMaster(PORT,HOST).client_connect())
        p.start()
        p.join()
