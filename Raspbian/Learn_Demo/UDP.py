#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import RPi.GPIO as GPIO
import socket

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(22, GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('10.10.100.83', 50000))

print('Bind UDP on 50000...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)

    result = data.decode('utf-8')

    print(result)
    if result == '01':
        print('let on')
        s.sendto(b'let on', ('10.10.100.40', 50000))
        # GPIO.output(22, GPIO.HIGH)
    else:
        print('let off')
        s.sendto(b'let off', ('10.10.100.40', 50000))
        # GPIO.output(22, GPIO.LOW)


