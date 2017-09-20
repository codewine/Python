
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。
# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)


# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，
# 直接通过sendto()给服务器发数据：

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
