import socket
import sys

PORT = int(sys.argv[1])

def transform(s):
    #s = str(s)
    s = s.upper()
    return s


with socket.socket() as sk:
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(("localhost", PORT))
    sk.listen()
    conn, addrs = sk.accept()
    
    data = conn.recv(1024)

    while True:
        if data == b"bye": break
        conn.sendall(transform(data))
        data = conn.recv(1024)
    
    sk.close()

