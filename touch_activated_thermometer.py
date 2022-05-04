import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)

while True:
    try:
        if GPIO.input(13):
            
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            print("Reading...")
            
            while GPIO.input(13):
                sleep(1)
            if humidity is not None and temperature is not None:
                print("Temp={0:0.1f}*F".format((temperature*9/5) + 32))
  
        else:
            print("Touch to activate!")
            while not GPIO.input(13):
                sleep(1)


    except:
        GPIO.cleanup()

    finally:
        pass
        