# -*- coding: utf-8 -*-

import time, threading

def heartBeatTimer():
    print('xintiao')

#
def Methond1():
    while True:
        print('UDP')
        time.sleep(2)
#
def Methond2():
    while True:
        print('TCP')
        time.sleep(3)
#
if __name__ == '__main__':
    UDPS = threading.Thread(target=Methond1(), args=())
    UDPS.start()

    print('test')

    TCPS = threading.Thread(target=Methond2(), args=())
    TCPS.start()