#basic socket programming
#client

import socket

#INET생성 스트림소켓
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
#웹서버에 접속
s.connect(("www.python.org", 80))


