# Written by Oleksandr Sofishchenko

# Simple socket programming in Python.
# The server sends the current time to the client
# Data transfer can changed directly in the code
# server.py

import socket
import time
#import sys

# creating socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# fetching local machine's name
server_address = ('localhost', 10000)

# bind to the port
serversocket.bind(server_address)

# listen up to 5 requests
serversocket.listen(5)

while True:
    # creating connection
    print("waiting for a connection")
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" %str(addr))
    currTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currTime.encode('ascii'))
    clientsocket.close()

