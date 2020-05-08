import socket
import sys
import json
from datetime import datetime

PORT = 8001
message = sys.argv[1]
access_key = "0laph"
user_id = "1234"
to = "1267"

client_request = {
    "user_id": user_id,
    "access_key": access_key,
    "message": message,
    "to": to,
    "request_dt": datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
}

with socket.socket() as sk:
    sk.connect(("localhost", PORT)) # connect
#    while True:
#        send = input("client>")
#        sk.sendall(bytes(send.encode("utf-8"))) # data out
#        if send == "bye": break
#        data = sk.recv(1024) # data in
#        print("received:", data) # output in terminal
    request = bytes(json.dumps(client_request).encode("utf-8"))
    sk.sendall(request)
    # data = sk.recv(1024)
    # print(data)
