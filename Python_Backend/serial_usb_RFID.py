#!/usr/bin/python3
 
import sys
import time
import serial
sys.path.append('./.local/lib/python3.9/site-packages')
import time
from datetime import datetime,date
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import messaging

"""
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

"""

def main():
	"""
	# initialize firebase, API for backend-UI communication
	cred = credentials.Certificate('service-account.json')
	default_app = firebase_admin.initialize_app(cred)
	"""

	# initialize serial python, framework for reading serial USB
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 115200,
		timeout = 10)
	
	# define token FCM
	MY_TOKEN = 'c5yjW1zvnlRmReBb3tMf1z:APA91bGUWucYXD3t76QScJyZYJlpSQikl312dNvgkfcDWNthDbwUrdsL0VHhP6ROdA7pvI0A8VgeSzIyVhEm-G2OKQnVyTZB_a4Tic_NFnSMzpUQCO4ZtKPoTkdNtjF8YK4AZ_AsImWA'

	# MAIN LOOP
	#print("Raspberry's receiving : ")

	while (True): 
		
		# read USB serial and convert to string  
		packet = bytearray()
		"""
		packet.append(0x02) # STX
		packet.append(0x00) # LEN-H
		packet.append(0x01) # LEN-L
		packet.append(0x22) # CMD
		packet.append(0x22) # LRC
		"""
		#REQAcommand = b'\x02\x00\x01\x21\x20'
		REQAcommand = b'\x20\x21\x01\x00\x02'
		WUPAcommand = b'\x23\x22\x01\x00\x02'
		ANCOcommand = b'\x23\x22\x01\x00\x02'
		
		
		
		if input("Select command: ")=='r':
			print(f"write to the card: {hex(int.from_bytes(REQAcommand,byteorder='little'))}\n")
			ser.write(REQAcommand) 
			#ser.write(WUPAcommand) 
			print(f"Done writing\n")
			
			"""
			cw = [0x00,0x01,0x21]
			ser.write(serial.to_bytes(cw))
			print(f"Done writing\n")
			"""
			
			# b'\x1a\xff'

			#print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")
			#in_bin = ser.readlines()
			in_bin = ser.read(size=32)
			print("Read binary:")
			print(in_bin)
			#print("Decoded binary:")
			#print(in_bin.decode("utf-8"))
			if in_bin != b'':
				in_hex = hex(int.from_bytes(in_bin,byteorder='big')) 
				print(f"hexa read: {in_hex}")
				#for i in range(10):
				#	print(f"id of the card: {in_hex}\n")
		
	

if __name__ == "__main__":
	main()
 

