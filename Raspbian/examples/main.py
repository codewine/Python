#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sakshat import SAKSHAT
import time
import subprocess
import sys

#Declare the SAKS Board
SAKS = SAKSHAT()
args = sys.argv
action = args[1]

if __name__ == "__main__":
    if action == "beep":
        SAKS.buzzer.beep(int(args[2]))
    if action == "ledon":
        if args[2] == "all":
            SAKS.ledrow.on()
        else:
            SAKS.ledrow.on_for_index(int(args[2]))
    if action == "ledoff":
        SAKS.ledrow.off()
    if action == "getledstatus":
        print(SAKS.ledrow.is_on(int(args[2])))
    if action == "displaynum":
        SAKS.digital_display.show(args[2])
    if action == "displayoff":
        SAKS.digital_display.off()