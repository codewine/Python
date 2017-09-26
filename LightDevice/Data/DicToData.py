# -*- coding: utf-8 -*-

from Metod import DeviceMsg
from Metod import Method
from GPIOMethod import GPIOMethod

messgeId = 0x00;
def getMessgeId():
    global messgeId
    messgeId = messgeId +1
    return messgeId


def dataWithHeaderBody(body):
    mac = DeviceMsg.getMac()
    data = bytearray()
    bodyData = body[1]
    header = haedrDataWithArr(mac,body)

    for b in header:
        data.insert(len(data),b)
    for b in bodyData:
        data.insert(len(data),b)

    return data


def haedrDataWithArr(mac,body):

    bodyData = body[1]
    length = len(bodyData)

    cmd = body[0]
    #
    data = bytearray()

    msgId = getMessgeId()

    for b in (0x40,0x02):
        data.insert(len(data), b)
    #
    for b in Method.intTO2BYtes(msgId):
        data.insert(len(data),b)
    #
    for b in (0xff,0x00):
        data.insert(len(data), b)
    #GroupId
    for b in DeviceMsg.getGroupId():
        data.insert(len(data), b)
    #
    for b in Method.intTO2BYtes(length):
        data.insert(len(data), b)
    #
    data.insert(len(data), cmd)
    #
    for b in mac:
        data.insert(len(data),b)
    #
    for b in (0x00,0x00):
        data.insert(len(data), b)
    #
    data.insert(len(data),checksum(bodyData))

    return data

# 设备心跳
def devHeartBeat():

    return 0x01,bytes([0x01])

# 设备发现
def discover():

    device = DeviceMsg.getNewDevice()
    return 0x00,device

# 设备控制
def GPIOSControlRevice():
    return 0x02,bytes([0xff])

# 设备状态
def GPIOStaues():

    on = GPIOMethod.GetGPIO()
    if on:
        return 0x03,bytes([0xff])
    else:
        return 0x03,bytes([0x00])
# 校验和
def checksum(body):
    sum = 0;
    for char in body:
        sum = char + sum
    return sum%256

def char_checksum(data, byteorder='little'):
    '''''
    char_checksum 按字节计算校验和。每个字节被翻译为带符号整数
    @param data: 字节串
    @param byteorder: 大/小端
    '''
    length = len(data)
    checksum = 0
    for i in range(0, length):
        x = int.from_bytes(data[i:i+1], byteorder, signed=True)
        if x>0 and checksum >0:
            checksum += x
            if checksum > 0x7F: # 上溢出
                checksum = (checksum&0x7F) - 0x80 # 取补码就是对应的负数值
        elif x<0 and checksum <0:
            checksum += x
            if checksum < -0x80: # 下溢出
                checksum &= 0x7F
        else:
            checksum +=x # 正负相加，不会溢出
        #print(checksum)

    return checksum


def TCPLogInData():
    # return b'40020102ff07070000010010f00000123456123456c000904bf430021ae6e30814662943fb61dd15'
    return bytearray.fromhex('40020102ff07070000010010f00000123456123456c000904bf430021ae6e30814662943fb61dd15')

def TCPHeartBeatData():
    # return b'40020102ff07070000010010f10000123456123456c000cb907396086761a5734ad1a11559d684c6'
    return bytearray.fromhex('40020102ff07070000010010f10000123456123456c000cb907396086761a5734ad1a11559d684c6')




# list() 将对象转换为list
#
# str() 将对象转换为str
#
# bytearray() 将对象转换为bytearray
#
# bytearray.fromhex() 将对象从hexstring转换为bytearray
#
# binascii.b2a_hex() 将对象从str转换为hexstring

# 1整形列表转str
def bytesToStr():
    x = [0x53, 0x21, 0x6A]
    y = str(bytearray(x))

# 2str转整形列表
def StrToBytes():
    x = '\x53\x21\x6a'
    y = [ord(c) for c in x]


# 3整形列表转换为hexstring
def bytesToHexStr():
    import binascii
    x = [0x53, 0x21, 0x6A]
    y = str(bytearray(x))
    z = binascii.b2a_hex(y)


#  4hex string转换为整形列表
def hexStrToBytes():
    x = '53216A'
    y = bytearray.fromhex(x)
    z = list(y)

# 5hexstring转换为str
def HexStrToStr():
    x = '53216A'
    y = bytearray.fromhex(x)
    z = str(y)
