from gpiozero import Servo
import math
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

go = True

while go:
    for i in range(0, 90):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)
    for i in range(90, 180):
        servo.value = math.sin(math.radians(i))
        sleep(0.1)
    for i in range(180, 270):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)
    for i in range(270, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.1)
    
        
        

  
        
