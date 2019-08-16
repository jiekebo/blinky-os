import RPi.GPIO as GPIO
import time

#LedPin = [4,17,18,27,22,23,24]

LedPin = [4]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in LedPin:
	GPIO.setup(pin, GPIO.OUT)

sleep = 3

try:
	while True:
		for pin in LedPin:
			GPIO.output(pin,GPIO.HIGH)
			time.sleep(sleep)
			GPIO.output(pin,GPIO.LOW)
			#time.sleep(sleep)
except KeyboardInterrupt:
	print "LED off"
	for pin in LedPin:
		GPIO.output(pin,GPIO.LOW)
