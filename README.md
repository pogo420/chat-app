# chat-app

App for chat application
####################### client side ##############################
(chat-app-env) arnab@arnab:~/chat-app$ python test-client.py "hello boss All cool?"
(chat-app-env) arnab@arnab:~/chat-app$ python test-client.py "yo bro"
(chat-app-env) arnab@arnab:~/chat-app$
code: test-client.py

####################### server side ##############################
(chat-app-env) arnab@arnab:~/chat-app$ python server-master-v1.py
serving client: ('127.0.0.1', 47094)
data received hello boss All cool?
serving client: ('127.0.0.1', 47096)
data received yo bro

code: server-master-v1.py
