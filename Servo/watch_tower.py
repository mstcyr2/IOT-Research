from gpiozero import Servo
from gpiozero import MotionSensor
import math
from time import sleep
import time
import smtplib

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
pir = MotionSensor(4)

servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

while True:
    if pir.wait_for_motion():
        go = True
    print("motion detected")
    while go :
        for i in range(0, 360):
            servo.value = math.sin(math.radians(i))
            sleep(0.01)
        if pir.wait_for_motion():
            go = True
        if pir.wait_for_no_motion():
            go = False
            print("No motion detected")                                                                       
            servo.value = None