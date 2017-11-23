#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 17
echo = 18
led = 22

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.output(trig, 0)

GPIO.setup(echo, GPIO.IN)

time.sleep(0.1)

try:
  while True:
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

    while GPIO.input(echo) == 0:
      pass
    start = time.time()

    while GPIO.input(echo) == 1:
      pass
    stop = time.time()

    dist = round((stop - start) * 17000)
    print(dist)

    if dist < 28:
      GPIO.output(led, 1)
    else:
      GPIO.output(led, 0)

    time.sleep(0.1)
finally:
  GPIO.cleanup()
