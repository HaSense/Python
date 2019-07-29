#가장 간단한 파이썬 파일전송 서버
import socket
import sys

#소켓을 만듭니다.
s = socket.socket()
#IP와 Port를 바인딩합니다.
s.bind(("172.30.1.11",9999))
#접속을 기다립니다.
s.listen(10) #10은 백로그(backlog)인데 accept()없이 대기 가능한 연결요청의 최대개수 입니다.

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
