from gpiozero import Servo
from gpiozero import MotionSensor
import math
from time import sleep
import time
import smtplib

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

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
pir = MotionSensor(4)

servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

while True:
    if pir.wait_for_motion():
        go = True
    print("motion detected")
    sendTo = ''
    emailSubject = "Watch Tower Servo Project"
    emailContent = "Motion Detected!"

    sender.sendmail(sendTo, emailSubject, emailContent)
    
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
