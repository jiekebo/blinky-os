#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = [4,17,18,27,22,23,24]
freq = 100
sleep = 0.007
ps = []

GPIO.setmode(GPIO.BCM)       # Numbers pins by physical location
for pin in LedPin:
    GPIO.setup(pin, GPIO.OUT)   # Set pin mode as output
    GPIO.output(pin, GPIO.LOW)  # Set pin to low(0V)

    ps.append(GPIO.PWM(pin, freq))     # set Frequece to 1KHz

for p in ps:
    p.start(0)                     # Start PWM output, Duty Cycle = 0

try:
        while True:
                for dc in range(1, 100, 1):   # Increase duty cycle: 0~100
			for p in ps:
                        	p.ChangeDutyCycle(dc)     # Change duty cycle
                        	time.sleep(sleep)
                time.sleep(1)
                for dc in range(100, -1, -1): # Decrease duty cycle: 100~0
			for p in ps:
                        	p.ChangeDutyCycle(dc)
                        	time.sleep(sleep)
                time.sleep(1)
except KeyboardInterrupt:
	for i,p in enumerate(ps):
        	p.stop()
        	GPIO.output(LedPin[i], GPIO.HIGH)    # turn off all leds
        	GPIO.cleanup()
