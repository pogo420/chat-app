import socket
import sys

PORT = int(sys.argv[1])

def transform(s):
    '''Function for some arbitary transform'''
    #s = str(s)
    s = s.upper()
    return s


with socket.socket() as sk:
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reusing port 
    sk.bind(("localhost", PORT)) # bind
    sk.listen() # listen
    conn, addrs = sk.accept() # accept 
    
    data = conn.recv(1024) # data in

    while True:
        if data == b"bye": break
        conn.sendall(transform(data)) # data out
        data = conn.recv(1024) # data in
    
    sk.close() # socket close; not required with "with" clause 

