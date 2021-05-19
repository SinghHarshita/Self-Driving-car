# TCP client
import socket

localIP   = "172.20.10.2"
localPort = 20001

bufferSize = 1024

bytesToSend = str.encode("Hello TCP Server")

# Create socket
TCPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

# Connect to the server
TCPClientSocket.connect((localIP, localPort))

flag = True

while flag:
    # Send data
    bytesToSend = input("\nEnter message : ").encode()
    TCPClientSocket.sendall(bytesToSend)
    
    # Receive data
    data = TCPClientSocket.recv(bufferSize).decode()
    print("Message from Server : ", repr(data))

    if data.find("bye") != -1:
        flag = False

# Close the connection
TCPClientSocket.close()