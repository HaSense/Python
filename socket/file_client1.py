import socket
import sys

s = socket.socket()
s.connect(("172.30.1.11", 9999))
f = open('ubuntu1604.iso', 'rb')
l = f.read(1024)
while(l):
    s.send(l)
    l = f.read(1024)

s.close()
