# -*- coding: utf-8 -*-

from Metod import DeviceMsg
from UDP import UDPServer
from UDP import Brocaster
from GPIOMethod import GPIOMethod
from TCP import TCPServer
from Data import DicToData
import threading
from Metod import Method

if __name__ == '__main__':

    TCPS = threading.Thread(target=TCPServer.StartTCP, args=())
    TCPS.start()

    Method.MyPrint('print')
    #
    UDPS = threading.Thread(target=UDPServer.StartUDP, args=())
    UDPS.start()


def handleUDP(socket,data,addr):
    try:
        result = data.decode('utf-8')
        if result == '01':
            Method.MyPrint('let on')
            GPIOMethod.OPenClose22(True)
            Brocaster.send(b'let on')
        else:
            Method.MyPrint('let off')
            GPIOMethod.OPenClose22(False)
            Brocaster.send(b'let off')
        pass
    except:

        if len(data) >= 24:
            #GroupId
            if data[6:10] == DeviceMsg.getGroupId():
                cmd = data[12]
                mac = data[13:21]
                Method.MyPrint('recvie cmd:%s mac:%s'%(cmd,mac))
                judgeUDPCmd(cmd,data[24:len(data)],mac)
        pass


def judgeUDPCmd(cmd,bodyData,mac):

    macSelf = DeviceMsg.getMac()
    # 设备发现
    if cmd == 0x00:
        Method.MyPrint('0x00')
        sendData = DicToData.dataWithHeaderBody(DicToData.discover())
        Brocaster.send(sendData)

    elif mac == macSelf:
        # 设备心跳
        if cmd == 0x01:
            Method.MyPrint('0x01')
            sendData = DicToData.dataWithHeaderBody(DicToData.devHeartBeat())
            Brocaster.send(sendData)
            pass

        # 设备控制
        elif cmd == 0x02:
            Method.MyPrint('0x02')
            if bodyData[0] == 0x00:
                GPIOMethod.OPenClose22(False)
                sendData = DicToData.dataWithHeaderBody(DicToData.GPIOSControlRevice())
                Brocaster.send(sendData)

            if bodyData[0] == 0xff:
                GPIOMethod.OPenClose22(True)
                sendData = DicToData.dataWithHeaderBody(DicToData.GPIOSControlRevice())
                Brocaster.send(sendData)
            pass

        # 设备上报
        elif cmd == 0x03:
            pass

        # 设备查询
        elif cmd == 0x04:
            Method.MyPrint('0x04')
            sendData = DicToData.dataWithHeaderBody(DicToData.GPIOStaues())
            Brocaster.send(sendData)
            pass
    else:
        pass



def handleTCP(socket,data,addr):
    try:
        result = data.decode('utf-8')
        if not data or data.decode('utf-8') == 'exit':
            socket.close()
    except:
        if len(data) >= 24:
            #GroupId
            if data[6:10] == DeviceMsg.getGroupId():
                cmd = data[12]
                Method.MyPrint('recvie cmd:%s'%cmd)
            else:
                pass
        pass;


def sendGPIOChange(isOn):
    # UDP
    sendData = DicToData.dataWithHeaderBody(DicToData.GPIOStaues())
    Brocaster.send(sendData)
    # tcp
    TCPServer.sendData(sendData)
    pass











