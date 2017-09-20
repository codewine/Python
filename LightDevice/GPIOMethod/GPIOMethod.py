# -*- coding: utf-8 -*-


import Manage
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(22, GPIO.OUT)

def OPenClose22(openClose):
    print(openClose)
    if openClose:
        # GPIO.output(22, GPIO.HIGH)
        Manage.sendGPIOChange(True)

    else:
        # GPIO.output(22, GPIO.LOW)
        Manage.sendGPIOChange(False)
    pass



def GetGPIO():
    #
    # if (GPIO.input(22) == 1):
    #     return True
    # else:
    #     return False

    return False
    pass


