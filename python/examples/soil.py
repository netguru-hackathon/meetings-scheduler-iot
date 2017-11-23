#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor = 17
relay  = 18

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

while True:
    if GPIO.input(sensor) == True:
        GPIO.output(relay, GPIO.LOW)
    else:
        GPIO.output(relay, GPIO.HIGH)

GPIO.cleanup()
