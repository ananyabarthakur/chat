import socket
from datetime import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

s.connect((host, port))
print("Connected to server")

x = True

while x is True:
    message = s.recv(1024)
    now = datetime.now()
    message = message.decode()
    print(str(now)+' server > ' +message)
    reply = input(str("Me > "))
    if reply == 'quit':
        s.send('Client is leaving chatroom'.encode())
        x = False
    s.send(reply.encode())

