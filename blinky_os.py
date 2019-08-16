#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

LED_PINS = [4,17,18,27,22,23,24]

def read_script(path):
    with open(path) as f:
        lines = f.readlines()
        speed = float(lines[0]) / 1000
        script = list(map(lambda row : row.strip(), lines[1:]))
        return speed, script

def command_led_off(idx):
    GPIO.output(LED_PINS[idx], GPIO.LOW)

def command_led_on(idx):
    GPIO.output(LED_PINS[idx], GPIO.HIGH)

def run_row(row):
    for idx, command in enumerate(row):
        if command == '0':
            command_led_off(idx)
        elif command == '*':
            command_led_on(idx)
        else:
            pass

def run_script(speed, script):
    i = 0
    while True:
        if i == len(script):
            i = 0
        row = script[i]
        print(f'blinky command {str(i).zfill(2)} {row}')

        time.sleep(speed)
        i += 1

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in LedPin:
	    GPIO.setup(pin, GPIO.OUT)

    args = sys.argv[1:]
    speed, script = read_script(args[0])
    run_script(speed, script)

if __name__ == "__main__":
    main()