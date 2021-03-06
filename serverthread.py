import socket
import sys
from datetime import datetime


all_connections = []
all_addresses = []

#Create socket

def create_socket():
    try:
        global host
        global port
        global s # s for socket
        host = '127.0.0.1'
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as message:
        print("socket creation error" + str(message))


def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        print("Binding port: " + str(port))
        s.listen(5)

    except socket.error as message:
        print("Socket binding error"+ str(message) + "\n")
        #bind_socket()
        # recursion

    global no_of_connections
    no_of_connections = input ("Enter number of clients: ")
    accepting_connection(no_of_connections)

# handling connections from multiple clients
def accepting_connection(n):
    #close previous connections
    #for c in all_connections:
        #c.close()

    #del all_connections[:]
    #del all_addresses[:]

    x = True
    count = 0

    while x is True:
        try:
            conn, addr = s.accept()
            count = count + 1
            print ("Connection " + str(count) +" has been established")

            #store these connections
            all_connections.append(conn)
            all_addresses.append(addr)
            print("connection stored")

            if count == n:
                x = False
        except:
            print ("Error accepting  connection")
            break
    

# send commands to client
def select_client():
    choice= input(str("Select connection to send message to (1-"+str(no_of_connections)+"), for broadcast enter 'broadcast':"))
    if choice == '1':
        conn = all_connections[0]
        send_message(conn)
    elif choice == '2':
        conn = all_connections[1]
        send_message(conn)
    elif choice == '3':
        conn = all_connections[2]
        send_message(conn)
    elif choice == 'broadcast':
        broadcast()
    else:
        print("Connection doesn't exist")

def send_message(conn):
    print ("Enter 'quit' to exit and 'back' to select another client")
    x = True
    while x is True:
        msg = input("Me > ")
        if msg == 'quit':
            conn.close()
            s.close()
            x = False
        elif msg == 'back':
            select_client()
        else:
            conn.send(msg.encode())
            reply = conn.recv(1024)
            now = datetime.now()
            reply = reply.decode()
            print(str(now) + ' client > ' + reply)

def broadcast():
    message = input ("Enter message to broadcast: ")
    for conn in all_connections:
        conn.send(message.encode())
    select_client()

def main():
    create_socket()
    bind_socket()
    select_client()
    

main()
