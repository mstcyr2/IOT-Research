#!/usr/bin/python3

import RPi.GPIO as GPIO
from signal import signal, SIGTERM, SIGHUP, pause
from smbus import SMBus
from time import sleep
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)



bus = SMBus(0)
ads7830_commands = (0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4)


def safe_exit(signum, frame):
    exit(1)

def read_ads7830(input):
    bus.write_byte(0x4b, ads7830_commands[input])
    return bus.read_byte(0x4b)


while True:
    try:
        if GPIO.input(13):
            
            print("Activated!")
            
            while GPIO.input(13):
                signal(SIGTERM, safe_exit)
                signal(SIGHUP, safe_exit)

                print(f"x: {read_ads7830(7)}, y: {read_ads7830(6)}")

                sleep(0.1)
        else:
            print("Touch to activate!")
            while not GPIO.input(13):
                sleep(1)


    except:
        GPIO.cleanup()

    finally:
        pass
        