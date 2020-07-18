import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

s.connect((host, port))
print("Connected to server")

x = True

while x is True:
    message = s.recv(1024)
    message = message.decode()
    print('server >' +message)
    reply = input(str("Me > "))
    if reply == "quit":
        s.close()
        x = False
    s.send(reply.encode())

