# -*- coding: utf-8 -*-
import socket
import time, threading
#服务器端


# 创建新线程
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        try:
            data,addr = s.recvfrom(1024)
            print('Received from %s:%s.' % addr)
            result = data.decode('utf-8')
            print(result)
            if result == '01':
                print('let on')
                s.sendto(b'let on', (addr, 5000))
                # GPIO.output(22, GPIO.HIGH)
            else:
                print('let off')
                s.sendto(b'let off', (addr, 5000))
                # GPIO.output(22, GPIO.LOW)
        except:
            pass


if __name__ == "__main__":
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    host="10.10.100.165" #修改为自己的ip
    s.bind((host, 16684))
    s.listen(5)
    print('Waiting for connection...')

    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()




