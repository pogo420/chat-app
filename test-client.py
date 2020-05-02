import socket
import sys

PORT = int(sys.argv[1])
message = sys.argv[2]


with socket.socket() as sk:
    sk.connect(("localhost", PORT)) # connect 
#    while True:
#        send = input("client>")
#        sk.sendall(bytes(send.encode("utf-8"))) # data out
#        if send == "bye": break
#        data = sk.recv(1024) # data in
#        print("received:", data) # output in terminal 
    sk.sendall(bytes(message.encode("utf-8")))
    

