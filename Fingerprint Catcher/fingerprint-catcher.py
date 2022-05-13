#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import smtplib
import tempfile
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME ='' 
GMAIL_PASSWORD = ''


msg = MIMEMultipart()
msg['From'] = GMAIL_USERNAME
msg['To'] = GMAIL_USERNAME
msg['Subject'] = "Fingerprint Catcher Project"

msg_content = MIMEText('Intruder Fingerprint', 'plain', 'utf-8')
msg.attach(msg_content)


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


## Search for a finger
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to search the finger and calculate hash
try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    ## Searchs template
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('Access Denied')
	print('Downloading intruder fingerprint...')
	imageDestination= tempfile.gettempdir() + '/fingerprint.png'
	f.downloadImage(imageDestination)

	with open(imageDestination, 'rb') as f:
	    # set attachment mime and file name, the image type is png
	    mime = MIMEBase('image', 'png', filename='fingerprint.png')
	    # add required header data:
	    mime.add_header('Content-Disposition', 'attachment', filename='fingerprint.png')
	    mime.add_header('X-Attachment-Id', '0')
	    mime.add_header('Content-ID', '<0>')
	    # read attachment file content into the MIMEBase object
	    mime.set_payload(f.read())
	    # encode with base64
	    encoders.encode_base64(mime)
	    # add MIMEBase object to MIMEMultipart object
	    msg.attach(mime)

	print('Sending image....')
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	server.starttls()
	server.set_debuglevel(1)
	server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
	server.sendmail(GMAIL_USERNAME, GMAIL_USERNAME, msg.as_string())
	server.quit()

        exit(0)
    else:
        print('Access Granted')
        print('The accuracy score is: ' + str(accuracyScore))

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
