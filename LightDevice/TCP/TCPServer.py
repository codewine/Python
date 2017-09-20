# -*- coding: utf-8 -*-

import socket
import os,sys
import threading
from Metod import Method
from TCP import CircleTimer
import Manage

class TCPManage():

    # 发送TCP
    def sendData(data):
        try:
            sockLocal.send(data)
        except:

            Method.MyPrint('TCP 发送失败')


# 发送TCP
def sendData(data):
    try:
        sockLocal.send(data)
    except:
        Method.MyPrint('TCP 发送失败')
        heartBeat.cancel()
        TCPRevice._stop()

# 心跳发送
def heartBeatTimer():
    try:
        data = '心跳'.encode('utf-8')
        sendData(data)
        Method.MyPrint('心跳发送')
    except:
        pass



# 创建新线程
def reviceData(s):

    while True:
        try:
            # 接收数据:
            data, addr = s.recvfrom(1024)
            if len(data) > 0:
                Method.MyPrint('Received from %s:%s.' %(data,addr))
                Manage.handleTCP(s, data, addr)
        except:
            pass

#
count = 0x00
def StartTCP():

    global count
    count += 1
    print('count',count)
    host,port = Method.getServerIPAndPort()
    global sockLocal
    sockLocal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Method.MyPrint('try connect to ', host, port)
    try:
        sockLocal.connect((host, port))
        Method.MyPrint('connect %s %d sucess' % (host, port))
        # TCP 连接成功
        TCPConnectSuccess()
    except:

        reTryConnect = threading.Timer(5, StartTCP)
        reTryConnect.start()
        pass;


def TCPConnectSuccess():
    # 定时发送
    global heartBeat
    heartBeat = CircleTimer.LoopTimer(3, heartBeatTimer, (sockLocal,))
    heartBeat.start()
    # 处理接收
    global TCPRevice
    TCPRevice = threading.Thread(target=reviceData,args=(sockLocal,))
    TCPRevice.start()





