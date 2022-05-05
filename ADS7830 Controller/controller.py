#!/usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
from smbus import SMBus
from time import sleep
from gpiozero import Servo
from spidev import SpiDev
import math

from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()
servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

spi = SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 35000000

bus = SMBus(1)
ads7830_commands = (0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4)


def safe_exit(signum, frame):
    exit(1)

def read_ads7830(input):
    bus.write_byte(0x4b, ads7830_commands[input])
    return bus.read_byte(0x4b)

def no_drift(input):
    value = read_ads7830(input)

    return value if value < 110 or value > 140 else 127 

def read_min(input):
    while True:
        value = read_ads7830(input)

        yield (127-value)/127 if value < 110 else 0

def read_max(input):
    while True:
        value = read_ads7830(input)

        yield (value-128)/127 if value > 140 else 0
        
while True:
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)

        print(f"x: {read_ads7830(7)}, y: {read_ads7830(6)}")
        
        x = no_drift(6)
        y = no_drift(7)
        
        pos = math.sqrt(x*x + y*y)
        
        servo.value = math.sin(math.radians(pos))

        sleep(0.1)

    except KeyboardInterrupt:
        pass

    finally:
        pass
