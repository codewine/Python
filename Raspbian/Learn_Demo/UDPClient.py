import socket
from socket import *
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

for data in [b'Michael', b'Tracy', b'Sarah']:

    # 发送数据:
    # s.sendto(data, ('255.255.255.255', 5000))
    s.sendto(data, ('10.10.100.165', 5000))
    print('send')
    # 接收数据:5000
    print(s.recv(1024).decode('utf-8'))
