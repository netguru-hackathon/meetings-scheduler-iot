#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    flag = GPIO.input(16)

    if flag == False:
        print('button pressed')
        time.sleep(0.2)

GPIO.cleanup()
