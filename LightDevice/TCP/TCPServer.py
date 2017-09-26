# -*- coding: utf-8 -*-

import socket
import os,sys
import threading
from Metod import Method
from TCP import CircleTimer
import Manage
from Data import DicToData

class TCPManage():

    # 发送TCP
    def sendData(data):
        try:
            print('TCP发送')
            sockLocal.send(data)
        except:

            Method.MyPrint('TCP 发送失败')


# 发送TCP
def sendData(data):
    try:
        print('tcp发送',data)
        sockLocal.send(data)
    except:
        Method.MyPrint('TCP 发送失败')
        if heartBeat.isAlive:
            heartBeat.cancel()
        if TCPRevice.isAlive:
            TCPRevice._stop
        try:
            StartTCP()
        except:
            pass

# 心跳发送
def heartBeatTimer():
    try:
        # data = '心跳'.encode('utf-8')
        # data = DicToData.dataWithHeaderBody(DicToData.devHeartBeat())
        data = DicToData.TCPHeartBeatData()
        sendData(data)
    except:
        pass


# 创建新线程
def reviceData():

    while True:
        try:
            # 接收数据:
            data, addr = sockLocal.recvfrom(1024)
            if len(data) > 0:
                Method.MyPrint('Received from %s:%s.' %(data,addr))
                Manage.handleTCP(sockLocal, data, addr)
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
        sockLocal.settimeout(10)
        sockLocal.connect((host, port))
        Method.MyPrint('connect %s %d sucess' % (host, port))
        # TCP 连接成功
        TCPConnectSuccess()
    except:
        print('failed')
        global reTryConnect
        # 如果存在,停止计时器
        try:
            reTryConnect.cancel()
        except:
            pass

        reTryConnect = threading.Timer(5, StartTCP)
        reTryConnect.start()
        pass


def TCPConnectSuccess():

    logInData = DicToData.TCPLogInData()
    sendData(logInData)

    #取消自动连接
    reTryConnect.cancel()
    # 定时发送
    global heartBeat
    heartBeat = CircleTimer.LoopTimer(3, heartBeatTimer, ())
    heartBeat.start()
    # 处理接收
    global TCPRevice
    TCPRevice = threading.Thread(target=reviceData,args=())
    TCPRevice.start()





