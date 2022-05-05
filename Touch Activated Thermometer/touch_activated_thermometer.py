import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep
import smtplib


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)

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

while True:
    try:
        if GPIO.input(13):
            
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            print("Reading...")
            
            read = GPIO.input(13)
            
            while read:
                sleep(3)
                read = False
            
            print("Remove touch")
            
            while GPIO.input(13):
                sleep(1)
                
            if humidity is not None and temperature is not None:
                print("Temp={0:0.1f}*F".format((temperature*9/5) + 32))
                
                sendTo = ''
                emailSubject = "Touch Activated Thermometer Project"
                emailContent = "Temp={0:0.1f}*F".format((temperature*9/5) + 32)

                sender.sendmail(sendTo, emailSubject, emailContent)
  
        else:
            print("Hold sensor to activate!")
            while not GPIO.input(13):
                sleep(1)


    except:
        GPIO.cleanup()

    finally:
        pass
        
