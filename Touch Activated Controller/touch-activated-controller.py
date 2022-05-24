#!/usr/bin/python3

import RPi.GPIO as GPIO
from signal import signal, SIGTERM, SIGHUP, pause
from smbus import SMBus
from time import sleep
import math
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


GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)


bus = SMBus(1)
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

            sendTo = ''
            emailSubject = "Touch Activated Controller Project"
            emailContent = "Controller activated!"

            sender.sendmail(sendTo, emailSubject, emailContent)
            
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
        
