import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import smtplib

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

motorPin1 = 13
motorPin2 = 11
enablePin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motorPin1, GPIO.OUT)
GPIO.setup(motorPin2, GPIO.OUT)
GPIO.setup(enablePin, GPIO.OUT)

p = GPIO.PWM(enablePin, 1000)
p.start(0)

GPIO.output(motorPin1, GPIO.HIGH)
GPIO.output(motorPin1, GPIO.LOW)
p.ChangeDutyCycle(50)
GPIO.output(enablePin, GPIO.HIGH)

startHum, startTemp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
fanON = []

SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME ='' 
GMAIL_PASSWORD = ''


class Emailer:
	def sendmail(self, recipient,  subject, content):
		#Creating the headers
		headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
			"To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
		headers = "\r\n".join(headers)

		#Connect to Gmail Server
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		session.ehlo()
		session.starttls()
		session.ehlo()

		#Login to Gmail
		session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

		#Send Email & Exit
		session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
		session.quit


sender = Emailer()



try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*F Humidity={1:0.1f}%".format((temperature*9/5) + 32, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
        
        if humidity > 80 :
            GPIO.output(motorPin1, GPIO.HIGH)
            GPIO.output(motorPin2, GPIO.LOW)
            p.ChangeDutyCycle(50)
            GPIO.output(enablePin, GPIO.HIGH)
            fanON.append("Temp={0:0.1f}*F Humidity={1:0.1f}%".format((temperature*9/5) + 32, humidity))
        else:
            GPIO.output(motorPin1, GPIO.LOW)
            GPIO.output(motorPin2, GPIO.LOW)
            GPIO.output(enablePin, GPIO.LOW)
            
except KeyboardInterrupt:
    sendTo = ''
    emailSubject = "Humidity Sensor w/ Fan Project"
    emailContent = "Starting: ("+ "Temp={0:0.1f}*F Humidity={1:0.1f}%".format((startTemp*9/5) + 32, startHum) + ") \n While fan is on: (" + str(fanON) + ")"

    sender.sendmail(sendTo, emailSubject, emailContent)
finally:
    GPIO.cleanup()

    
    
