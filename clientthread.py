import socket
import os
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

s.connect((host, port))
print("Connected to server")

while True:
    message = s.recv(1024)
    message = message.decode()
    print("server >", message)
    reply = input(str("Me > "))
    if reply == "quit":
        reply= "Leaving the Chat room"
        s.send(reply.encode())
        s.close()
        break
    s.send(reply.encode())

