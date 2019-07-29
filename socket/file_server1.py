import socket
import sys
s = socket.socket()
s.bind(("172.30.1.11",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while (True):
    sc, address = s.accept()

    print(address)
    i=1
    f = open('file_'+ str(i)+".iso",'wb') # Open in binary
    i=i+1

    l = sc.recv(1024)
    while (l):
        f.write(l)
        l = sc.recv(1024)
    f.close()
    sc.close()

s.close()
