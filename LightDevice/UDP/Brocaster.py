# -*- coding: utf-8 -*-
from socket import *
from Metod import Method
def send(data):
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    if len(data):
        host = Method.get255BroadAddList()
        port = Method.port()
        print('send to',host,port)
        s.sendto(data,(host,port))

    else:
        print('数据为空')