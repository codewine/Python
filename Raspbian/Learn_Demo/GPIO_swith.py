#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

i = 0
while i < 100:
    if i%2==0:
        print('let on')
        GPIO.output(22, GPIO.HIGH)
    else:
        print('let off')
        GPIO.output(22, GPIO.LOW)

    i += 1
    time.sleep(5)
GPIO.cleanup()