
# -*- coding: utf-8 -*-

import socket
from Metod import Method
import Manage
import time, threading

def StartUDP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = Method.port()
    try:
        # 绑定端口:
        s.bind(('', port))  # 不添加host表示接受广播
        Method.MyPrint(Method.getSelfIP())
        Method.MyPrint('wating for UDP message')
        h = threading.Thread(target=reviceData, args=(s,))
        h.start()
    except ValueError as e:
        Method.MyPrint('Bind to port %s failed du to %s'%(port,e))
        pass


def reviceData(s):
        while True:
            # 接收数据:
            data, addr = s.recvfrom(1024)
            myIP = Method.getSelfIP()
            # 判断是否为自己IP
            if addr[0] == myIP:
                Method.MyPrint('udp from self')
                pass
            else:
                Manage.handleUDP(s, data,addr)



# 未用代码
def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
    """Set TCP keepalive on an open socket.

    It activates after 1 second (after_idle_sec) of idleness,
    then sends a keepalive ping once every 3 seconds (interval_sec),
    and closes the connection after 5 failed ping (max_fails), or 15 seconds
    """
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)

def set_keepalive_osx(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
    """Set TCP keepalive on an open socket.

    sends a keepalive ping once every 3 seconds (interval_sec)
    """
    # scraped from /usr/include, not exported by python's socket module
    TCP_KEEPALIVE = 0x10
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, TCP_KEEPALIVE, interval_sec)

