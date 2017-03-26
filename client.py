# Written by Oleksandr Sofishchenko

# Simple socket programming in Python.
# Server socket does not receive any data. Instead, it produces
# client sockets.
# client.py

import socket

# create a socket object
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# fetching local machine's name
server_address = ("localhost", 10000)

# connection to hostname on the port
skt.connect(server_address)

# receive no more than 1024 bytes
tm = skt.recv(1024)

skt.close()

print("The time got from the server is %s" %tm.decode("ascii"))