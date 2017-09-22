# -*- coding: utf-8 -*-

import subprocess
import re
import socket

import datetime
def MyPrint(*args):
    time_stamp = datetime.datetime.now()
    print (time_stamp.strftime('%H:%M:%S'),args)


# from time import ctime
# def MyPrint(*args):
#     print (ctime(),args)

def intTO2BYtes(num):

    if num < 0xff:
        return 0x00,num
        pass
    elif num > 0xffff:
        pass
        return 0xff,0xff
    else:
        return 0xff,num - 0xff


# 服务器地址
def getServerIPAndPort():
    return '10.10.100.198',16684

# port
def port():
    return 6225

def getSelfIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# 获取ip
def get_host_ip():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    print('wifiName:',myname)
    return myaddr

# 获取广播地址
def get255BroadAddList():
    return '255.255.255.255'

# 获取广播地址
def getBroadAddList():
    ######获取IP以及子网掩码
    #######windows 下的命令是ipconfig,LINUX下是ifconfig,倘若再不行，我们直接用python获取ip
    try:
        try:sys_cmd = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)
        except:sys_cmd = subprocess.Popen('ifconfig',stdout=subprocess.PIPE)
    except:#####如果用ipconfig命令无法获取到机器的ip,使用python的socket模块获取
        ip_add = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        index_ = ip_add.rfind(".")
        return [ip_add[:index_]+".255"]
    cmd_res = sys_cmd.stdout.read()
    pattern = re.compile(r'((\d+\.){3}\d+\s)') #########正则匹配
    ip_list = pattern.findall(cmd_res)
    ip_add = []
    for i in ip_list:
        if int(i[0].rstrip().split(".")[-1]) == 0:
            subMask = str(i[0])
        else:
            ip_info = i[0][:i[0].rfind(".")]
            if ip_info not in ip_add:ip_add.append(ip_info)
    #########计算广播地址
    broad_list = []
    for j in ip_add:
        subMask_split = subMask.split(".")
        myIp = (j+".1").split(".")
        str_cast = ""
        for i in range(4):
            xx = (int(myIp[i])&int(subMask_split[i]))|((int(subMask_split[i]))^255)
            str_cast = str_cast + str(xx)+"."
        broad_list.append(str_cast.rstrip("."))

    print(broad_list)
    return broad_list

