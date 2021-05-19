# TCP Server Script

import socket

localIP   = "192.168.1.104"
localPort = 20001

#print("hello")

bufferSize = 1024

bytesToSend = str.encode("Hello TCP Client")

# Create Socket
TCPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

# Bind the socket
TCPServerSocket.bind((localIP, localPort))
print("TCP Server up and listening")

# Listen from client
TCPServerSocket.listen(5)

# Accept the incoming connection call
conn, addr = TCPServerSocket.accept()

flag = True

while flag:
    data = conn.recv(bufferSize).decode("ascii")

    print("Message from client : ", data)
    print("Client IP Address : ", addr)
    
    bytesToSend = input("\nEnter message : ").encode()
    
    if data.find("bye") != -1:
        flag = False

    conn.sendall(bytesToSend)

conn.close()