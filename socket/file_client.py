import socket
import sys

sock = socket.socket()
sock.connect(("127.0.0.1", 8081))
f = open('sudoku.png', 'rb')
data = f.read(1024)
while(data):
    sock.send(data)
    data = f.read(1024)

sock.send(b'') #block 방지를 위해 공백전송

sock.close()