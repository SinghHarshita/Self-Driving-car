from django.shortcuts import render, redirect
# from urllib.request import urlopen

# Create your views here.
import socket
# conn = ""

# Thingspeak API
# APIkey = "2O0L57XKSJE58ENR"
# baseURL = "https://api.thingspeak.com/update?api_key=2O0L57XKSJE58ENR"

def index(request):
    return render(request,"index.html")

localIP   = "192.168.1.105"
localPort = 20001

print("hello")

bufferSize = 1024

bytesToSend = str.encode("Hello TCP Client")

# Create Socket
TCPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

# Bind the socket
TCPServerSocket.bind((localIP, localPort))
print("TCP Server up and listening")

# Listen from client
TCPServerSocket.listen(5)

conn, addr = TCPServerSocket.accept()

def stream(request):
    # bytesToSend = "1".encode()
    # conn.sendall(bytesToSend)
    send()
    return render(request, "stream.html")

def send():
    bytesToSend = "1".encode()
    conn.sendall(bytesToSend)
    # conn = urlopen(baseURL + '&field1=1')

def stop(request):
    bytesToSend = "0".encode()
    conn.sendall(bytesToSend)
    # conn = urlopen(baseURL + '&field1=0')
    return redirect("/")