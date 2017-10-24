
import RPi.GPIO as GPIO
import time

def startIndicatorlight():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)

    i = 0
    while i < 100:
        if i % 2 == 0:
            print('let on')
            GPIO.output(20, GPIO.HIGH)
        else:
            print('let off')
            GPIO.output(20, GPIO.LOW)

        i += 1
        time.sleep(5)
    GPIO.cleanup()
