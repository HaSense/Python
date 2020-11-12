import socket
import sys

#소켓을 만듭니다.
server = socket.socket()
#IP와 Port를 바인딩합니다.
server.bind(("127.0.0.1",8081))
#접속을 기다립니다.
server.listen(10) #10은 백로그(backlog)인데 accept()없이 대기 가능한 연결요청의 최대개수 입니다.

while (True):
    client_sock, address = server.accept()

    print(address)
    i=1
    f = open('file_'+ str(i)+".png",'wb') # Open in binary
    i=i+1

    data = client_sock.recv(1024)
    while (data):
        f.write(data)
        data = client_sock.recv(1024)

    print('모든 파일을 모두 받았습니다.')    
    f.close()
    client_sock.close()
    sys.exit()
