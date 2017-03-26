# Written by Oleksandr Sofishchenko

# An echo server that echoes back all data to client
# that send it.
# echo_server.py

import socket

host = ""       # symbolic name meaning all available interfaces
port = 12345    # arbitrarily non-privileged port

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

skt.bind((host, port))
skt.listen(1)

conn, addr = skt. accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()