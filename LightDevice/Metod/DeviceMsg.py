# -*- coding: utf-8 -*-
from Metod import Method

class device(object):

    def __init__(self,IP,MAC,Dev_Type,Version,Ext):

        if isinstance(IP,bytes) and len(IP) == 4:
            self.IP = IP;
        else:
            print('IP类型为bytes,长度为4')

        if isinstance(MAC,bytes) and len(MAC) == 6:
            self.MAC = MAC;
        else:
            print('IP类型为bytes,长度为6')

        if isinstance(Dev_Type,bytes) and len(Dev_Type) == 1:
            self.Dev_Type = Dev_Type;
        else:
            print('IP类型为bytes,长度为1')

        if isinstance(Version,bytes) and len(Version) == 2:
            self.Version = Version;
        else:
            print('IP类型为bytes,长度为2')

        if isinstance(Ext,bytes):
            self.Ext = Ext;


# 获取ip
def getGroupId():
    return bytes([0x00,0x00,0x00,0x00])

# 地址
def getMac():
    return bytes([0x00,0x00,0xaa,0xbb,0xcc,0xdd,0xee,0xff])

# 设备类型
def getDev_Type():
    return bytes([0x12])

# 版本
def getVersion():
    return bytes([0x01,0x00])

# ext
def getExt():
    return bytes();

# 获取ip
def getIP():
    myaddr = Method.getSelfIP()
    tumple = myaddr.split('.')
    a = int(tumple[0])
    b = int(tumple[1])
    c = int(tumple[2])
    d = int(tumple[3])
    return bytes([a,b,c,d])


def getNewDevice():
    IP = getIP()
    MAC = getMac()
    Dev_Type = getDev_Type()
    Version = getVersion()
    Ext = getExt()

    devieBytes = bytearray()
    for b in IP:
        devieBytes.insert(len(devieBytes),b)
    for b in Dev_Type:
        devieBytes.insert(len(devieBytes),b)
    for b in Version:
        devieBytes.insert(len(devieBytes),b)
    for b in Ext:
        devieBytes.insert(len(devieBytes),b)
    print(len(devieBytes))
    return devieBytes

if __name__ == '__main__':
    device = getNewDevice()
    print(device)





