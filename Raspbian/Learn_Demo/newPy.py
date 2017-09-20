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
            pass
        except:
            main()
            break
            pass

# 创建新线程
def reviceData(sock):
    while True:
        data = sock.recv(1024)
        if data:
            print('Accept data ')
            print(data.decode('utf-8'))

        if data.decode('utf-8') == 'exit':
            sock.close()
            break

def main():
    host,port = "10.10.100.165",5000
    print (host,port)
    sockLocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        sockLocal.connect((host,port))
    except:
    	time.sleep(10)
    	main()
    	return
    h = threading.Thread(target=timer, args=(5, sockLocal))
    h.start()
    # 处理接收
    t = threading.Thread(target=reviceData, args=(sockLocal,))
    t.start()

if __name__ == "__main__" :
    main()











