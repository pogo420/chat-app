import socket
import sys

PORT = int(sys.argv[1])



with socket.socket() as sk:
    sk.connect(("localhost", PORT))
    while True:
        send = input("client>")
        sk.sendall(bytes(send.encode("utf-8")))
        if send == "bye": break
        data = sk.recv(1024)
        print("received:", data)


