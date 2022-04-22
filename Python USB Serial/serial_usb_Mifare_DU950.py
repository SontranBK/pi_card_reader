#!/usr/bin/python3
 
import sys
import time
import serial
sys.path.append('./.local/lib/python3.9/site-packages')
import time
from datetime import datetime,date
import codecs
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
		timeout = 1)
	
	# define token FCM
	MY_TOKEN = 'c5yjW1zvnlRmReBb3tMf1z:APA91bGUWucYXD3t76QScJyZYJlpSQikl312dNvgkfcDWNthDbwUrdsL0VHhP6ROdA7pvI0A8VgeSzIyVhEm-G2OKQnVyTZB_a4Tic_NFnSMzpUQCO4ZtKPoTkdNtjF8YK4AZ_AsImWA'

	# MAIN LOOP
	#print("Raspberry's receiving : ")


	#print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")
            
	# read USB serial and convert to string
	REQAcommand = bytearray()
	REQAcommand.append(0x02) # STX
	REQAcommand.append(0x00) # LEN-H
	REQAcommand.append(0x01) # LEN-L
	REQAcommand.append(0x21) # REQA CMD
	REQAcommand.append(0x20) # LRC

	WUPAcommand = bytearray()
	WUPAcommand.append(0x02) # STX
	WUPAcommand.append(0x00) # LEN-H
	WUPAcommand.append(0x01) # LEN-L
	WUPAcommand.append(0x22) # WUPA CMD
	WUPAcommand.append(0x23) # LRC

	ANCOcommand = bytearray()
	ANCOcommand.append(0x02) # STX
	ANCOcommand.append(0x00) # LEN-H
	ANCOcommand.append(0x01) # LEN-L
	ANCOcommand.append(0x23) # REQA CMD
	ANCOcommand.append(0x22) # LRC
	

	AUTHcommand = bytearray()
	AUTHcommand.append(0x02) # STX
	AUTHcommand.append(0x00) # LEN-H
	AUTHcommand.append(0x08) # LEN-L
	AUTHcommand.append(0x30) # AUTH CMD
	AUTHcommand.append(0x00) # AUTH with key A
	for i in range(6):
		AUTHcommand.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
	AUTHcommand.append(0x01) # Block number of the card
	AUTHcommand.append(0x39) # LRC
	

	READcommand = bytearray()
	READcommand.append(0x02) # STX
	READcommand.append(0x00) # LEN-H
	READcommand.append(0x02) # LEN-L
	READcommand.append(0x27) # REQA CMD
	READcommand.append(0x01) # # Block number of the card
	READcommand.append(0x24) # LRC


	READKEYcommand = bytearray()
	READKEYcommand.append(0x02) # STX
	READKEYcommand.append(0x00) # LEN-H
	READKEYcommand.append(0x0A) # LEN-L
	READKEYcommand.append(0x36) # REQA CMD
	READKEYcommand.append(0x00) # R mode
	READKEYcommand.append(0x00) # A mode
	READKEYcommand.append(0x00) # Block number of the card
	for i in range(6):
		READKEYcommand.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
	READKEYcommand.append(0x3c) # LRC

	#REQAcommand = b'\x02\x00\x01\x21\x20'
	#REQAcommand = b'\x20\x21\x01\x00\x02'
	#WUPAcommand = b'\x23\x22\x01\x00\x02'
	#ANCOcommand = b'\x23\x22\x01\x00\x02'
	
	# test with car NO.029
	
	"""
	while (True): 
		
		input_char = input("\nSelect command: ");
		if input_char =='rq':
			print(f"write to the card: {hex(int.from_bytes(REQAcommand,byteorder='big'))}")
			ser.write(REQAcommand) 
			print(f"Done writing")

			in_bin = ser.read(size=64)
			print("Read binary:")
			print(in_bin)
			in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
			#print(f"hexa read: {in_hex}")
			if in_bin == b'\x02\x00\x03\x00\x04\x00\x07' :
				print("REQA command succeded")
			else:
				print("REQA fail !!! Try REQA command again")

		elif input_char =='w':
			print(f"write to the card: {hex(int.from_bytes(WUPAcommand,byteorder='big'))}")
			ser.write(WUPAcommand) 
			print(f"Done writing")

			in_bin = ser.read(size=32)
			print("Read binary:")
			print(in_bin)
			in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
			#print(f"hexa read: {in_hex}")
			if in_bin == b'\x02\x00\x03\x00\x04\x00\x07' :
				print("REQA command succeded")
			else:
				print("REQA fail !!! Try REQA command again")
                                
		elif input_char =='ac':
			print(f"write to the card: {hex(int.from_bytes(ANCOcommand,byteorder='big'))}")
			ser.write(ANCOcommand) 
			print(f"Done writing")

			in_bin = ser.read(size=32)
			print("Read binary:")
			print(in_bin)
			in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
			#print(f"hexa read: {in_hex}")
			if in_bin == b'\x02\x00\x05\x00U\x14\xaf\\\xb7' :
				print("ANCO command succeded")
			else:
				print("ANCO fail !!! Try ANCO command again")

		elif input_char =='au':
			print(f"write to the card: {hex(int.from_bytes(AUTHcommand,byteorder='big'))}")
			ser.write(AUTHcommand) 
			print(f"Done writing")

			in_bin = ser.read(size=32)
			print("Read binary:")
			print(in_bin)
			in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
			#print(f"hexa read: {in_hex}")
			if in_bin == b'\x02\x00\x05\x00U\x14\xaf\\\xb7' :
				print("AUTH command succeded")
			else:
				print("AUTH fail !!! Try AUTH command again")

		elif input_char =='re':
			print(f"write to the card: {hex(int.from_bytes(READcommand,byteorder='big'))}")
			ser.write(READcommand) 
			print(f"Done writing")

			in_bin = ser.read(size=32)
			print("Read binary:")
			print(in_bin)
			in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
			#print(f"hexa read: {in_hex}")
			if in_bin == b'\x02\x00\x05\x00U\x14\xaf\\\xb7' :
				print("READ command succeded")
			else:
				print("READ fail !!! Try READ command again")

		elif input_char =='rek':
			print(f"write to the card: {hex(int.from_bytes(READKEYcommand,byteorder='big'))}")
			ser.write(READKEYcommand) 
			print(f"Done writing")

			in_bin = ser.read(size=32)
			print("Read binary:")
			print(in_bin)
			in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
			print(f"hexa read: {in_hex}")
			if in_bin == b'\x02\x00\x15\x00U\x14\xaf\\U\x14\xaf\\\xb2\x08\x04\x00\x02]\x84\xe9\x16\xa9\t\x1d2' :
				print("READ KEY command succeded")
			else:
				print("READ KEY fail !!! Try READ KEY command again")
	"""
	
	while (True): 

		#print(f"write to the card: {hex(int.from_bytes(READKEYcommand,byteorder='big'))}")
		ser.write(READKEYcommand) 
		#print(f"Done writing")

		in_bin = ser.read(size=32)
		#print("Read binary:")
		#print(in_bin)
		#print(f"hexa read: {in_hex}, type: {type(in_hex)}")
		in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
		#if in_bin == b'\x02\x00\x15\x00U\x14\xaf\\U\x14\xaf\\\xb2\x08\x04\x00\x02]\x84\xe9\x16\xa9\t\x1d2' :
		if in_hex[2:9] == '2001500':
			print("READ KEY command succeded")
			print(f"hexaread: {in_hex}, type: {type(in_hex)}")
			print(f"hexa 2:8 read: {in_hex[2:9]}")
			print(f"hexa 15:-2 read: {in_hex[15:-2]}")
			#ASCII = bytes.fromhex(in_hex[9:-2]).decode()
			ASCII = codecs.decode(in_hex[15:-2],"hex")
			print(f"ASCII code: {ASCII}")
		#else:
		#	print("READ KEY fail !!! Try READ KEY command again")

	

if __name__ == "__main__":
	main()
 

