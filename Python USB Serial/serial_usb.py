#!/usr/bin/python3
 
import sys
import time
import serial
sys.path.append('./.local/lib/python3.9/site-packages')
import time
from datetime import datetime,date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging


def send_all(title,body,FCM_token):
	# [START send_all]
	# Create a list containing up to 500 messages.
	messages = [
	messaging.Message(
	    notification=messaging.Notification(title, body),
	    token=FCM_token,
	),

	#messaging.Message(
	#    notification=messaging.Notification('Price drop', '2% off all books'),
	#    topic='readers-club',
	#),

	]

	response = messaging.send_all(messages)
	# See the BatchResponse reference documentation
	# for the contents of response.
	print('{0} messages were sent successfully'.format(response.success_count))
	# [END send_all]



def main():
	# initialize firebase, API for backend-UI communication
	cred = credentials.Certificate('service-account.json')
	default_app = firebase_admin.initialize_app(cred)

	# initialize serial python, framework for reading serial USB
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 9600,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 1)
	
	# define token FCM
	MY_TOKEN = 'c5yjW1zvnlRmReBb3tMf1z:APA91bGUWucYXD3t76QScJyZYJlpSQikl312dNvgkfcDWNthDbwUrdsL0VHhP6ROdA7pvI0A8VgeSzIyVhEm-G2OKQnVyTZB_a4Tic_NFnSMzpUQCO4ZtKPoTkdNtjF8YK4AZ_AsImWA'

	# MAIN LOOP
	print("Raspberry's receiving : ")

	while (True): 
		# read USB serial and convert to string   
		s = ser.readline()
		print(f"ser.readline: {s}")
		data = s.decode("utf-8")	# decode s
		print(f"s.decode: {data}")
		id_card = data.rstrip()	# cut "\r\n" at last of string
		print(f"{id_card[1:11]}\n")	# print string   
		
	

if __name__ == "__main__":
	main()
 

