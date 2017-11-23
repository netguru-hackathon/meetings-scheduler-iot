#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ControlPin = [17,18,22,23]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

seq1 = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

seq2 = [ [1,0,0,0],
        [1,0,0,1],
        [0,0,0,1],
        [0,0,1,1],
        [0,0,1,0],
        [0,1,1,0],
        [0,1,0,0],
        [1,1,0,0] ]

for x in range(10):

    for i in range(32):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq1[halfstep][pin])
            time.sleep(0.001 * (x+1))

    for i in range(32):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq2[halfstep][pin])
            time.sleep(0.001 * (x+1))

GPIO.cleanup()

