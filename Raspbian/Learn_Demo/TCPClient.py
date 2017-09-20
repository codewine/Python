# -*- coding: utf-8 -*-

import socket
import time, threading
import os,sys

def timer(n,s):
    while True:
        data = '心跳'.encode('utf-8')
        try:
            s.send(data)
            print('心跳发送')
            time.sleep(n)
        except:
            main()
            break



# 创建新线程
def reviceData(sock):
    print('Accept data ')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
    sock.close()

def main():

    host,port = '10.10.100.165',16684
    print (host,port)
    sockLocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockLocal.connect((host, port))
    # 定时发送
    h = threading.Thread(target=timer, args=(5,sockLocal))
    h.start()
    # # 处理接收
    # t = threading.Thread(target=reviceData)
    # t.start()


if __name__ == "__main__" :
    main()











