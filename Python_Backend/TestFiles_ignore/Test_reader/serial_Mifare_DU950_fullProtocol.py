#!/usr/bin/python3
 
"""
This is a serial Mifare DU-950 python code
full protocol
"""

import sys
import time
sys.path.append('./.local/lib/python3.9/site-packages')
import serial
import time
from datetime import datetime,date
import codecs

def main():
	

	# initialize serial python, framework for reading serial USB
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 115200,
		timeout = 0.05)
	

	#print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")
	"""
	Check out protocol Duali file for protocol information
	All command below must have STX and LRC in font and back
	Read "Communication Protocol Frame Format" in page 9 for STX and LRC information
	"""
	# read USB serial and convert to string
	# Command no.21
	REQAcommand = bytearray()
	REQAcommand.append(0x02) # STX
	REQAcommand.append(0x00) # LEN-H
	REQAcommand.append(0x01) # LEN-L
	REQAcommand.append(0x21) # REQA CMD
	REQAcommand.append(0x20) # LRC

	# Command no.22
	WUPAcommand = bytearray()
	WUPAcommand.append(0x02) # STX
	WUPAcommand.append(0x00) # LEN-H
	WUPAcommand.append(0x01) # LEN-L
	WUPAcommand.append(0x22) # WUPA CMD
	WUPAcommand.append(0x23) # LRC
	
	# Command no.13
	BUZZ1command = bytearray()
	BUZZ1command.append(0x02) # STX
	BUZZ1command.append(0x00) # LEN-H
	BUZZ1command.append(0x02) # LEN-L	
	BUZZ1command.append(0x13) # BUZZ1 CMD
	BUZZ1command.append(0x03) # BUZZ1 with tone and time
	BUZZ1command.append(0x01) # Octave 
	BUZZ1command.append(0x00) # Frequency
	BUZZ1command.append(0x10) # Time
	BUZZ1command.append(0x03) # LRC
	
	
	BUZZ2command = bytearray()
	BUZZ2command.append(0x02) # STX
	BUZZ2command.append(0x00) # LEN-H
	BUZZ2command.append(0x02) # LEN-L	
	BUZZ2command.append(0x13) # BUZZ2 CMD
	BUZZ2command.append(0x00) # BUZZ2 On
	BUZZ2command.append(0x11) # LRC
	
	BUZZ3command = bytearray()
	BUZZ3command.append(0x02) # STX
	BUZZ3command.append(0x00) # LEN-H
	BUZZ3command.append(0x02) # LEN-L	
	BUZZ3command.append(0x13) # BUZZ3 CMD
	BUZZ3command.append(0x01) # BUZZ3 Off
	BUZZ3command.append(0x10) # LRC
	
	LED1command = bytearray()
	LED1command.append(0x02) # STX
	LED1command.append(0x00) # LEN-H
	LED1command.append(0x02) # LEN-L	
	LED1command.append(0x13) # LED1 CMD
	LED1command.append(0x10) # LED1 Control
	LED1command.append(0x01) # LED1 position and on
	LED1command.append(0x00) # LRC
	
	LED2command = bytearray()
	LED2command.append(0x02) # STX
	LED2command.append(0x00) # LEN-H
	LED2command.append(0x02) # LEN-L	
	LED2command.append(0x13) # LED2 CMD
	LED2command.append(0x10) # LED2 Control
	LED2command.append(0x00) # LED2 Position and off
	LED2command.append(0x01) # LRC

	# Command no.23
	ANCOcommand = bytearray()
	ANCOcommand.append(0x02) # STX
	ANCOcommand.append(0x00) # LEN-H
	ANCOcommand.append(0x01) # LEN-L
	ANCOcommand.append(0x23) # ANCO CMD
	ANCOcommand.append(0x22) # LRC
	
	# Command no.30
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
	
	# Command no.27
	READcommand = bytearray()
	READcommand.append(0x02) # STX
	READcommand.append(0x00) # LEN-H
	READcommand.append(0x02) # LEN-L
	READcommand.append(0x27) # READ CMD
	READcommand.append(0x01) # # Block number of the card
	READcommand.append(0x24) # LRC

	# Command no.36 for block 4
	READKEY4command = bytearray()
	READKEY4command.append(0x02) # STX
	READKEY4command.append(0x00) # LEN-H
	READKEY4command.append(0x0A) # LEN-L
	READKEY4command.append(0x36) # REQA CMD
	READKEY4command.append(0x00) # R mode
	READKEY4command.append(0x00) # A mode
	READKEY4command.append(0x04) # Block number of the card
	for i in range(6):
		READKEY4command.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
	READKEY4command.append(0x38) # LRC
	
	# Command no.36 for block 5
	READKEY5command = bytearray()
	READKEY5command.append(0x02) # STX
	READKEY5command.append(0x00) # LEN-H
	READKEY5command.append(0x0A) # LEN-L
	READKEY5command.append(0x36) # REQA CMD
	READKEY5command.append(0x00) # R mode
	READKEY5command.append(0x00) # A mode
	READKEY5command.append(0x05) # Block number of the card
	for i in range(6):
		READKEY5command.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
	READKEY5command.append(0x39) # LRC

	# Command no.36 for block 6
	READKEY6command = bytearray()
	READKEY6command.append(0x02) # STX
	READKEY6command.append(0x00) # LEN-H
	READKEY6command.append(0x0A) # LEN-L
	READKEY6command.append(0x36) # REQA CMD
	READKEY6command.append(0x00) # R mode
	READKEY6command.append(0x00) # A mode
	READKEY6command.append(0x06) # Block number of the card
	for i in range(6):
		READKEY6command.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
	READKEY6command.append(0x3a) # LRC

	
	
	while (True): 
		command = input("Please insert 1 of following commands:\n"
						"- rk4: read block 4 of Mifare card with Key included\n")

		if command == "readkey":
			try:
				dataB4 = ""
				dataB5 = ""
				dataB6 = ""
				ser.write(READKEY4command) 
				in_hexB4 = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
				if in_hexB4[2:9] == '2001500':
					dataB4 = str(codecs.decode(in_hexB4[17:49], "hex"),'utf-8')		
					ser.write(READKEY5command)
					in_hexB5 = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
					if in_hexB5[2:9] == '2001500':
						dataB5 = dataB4 + str(codecs.decode(in_hexB5[17:49], "hex"),'utf-8')			
						ser.write(READKEY6command)		
						in_hexB6 = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
						if in_hexB6[2:9] == '2001500':
							dataB6 = dataB5 + str(codecs.decode(in_hexB6[17:49], "hex"),'utf-8')	
							print(f"data: {dataB6}")
							ser.write(BUZZ2command)
							time.sleep(0.15)
							ser.write(BUZZ3command)
						try:
							class_name = dataB6[:dataB6.index("|")]
							rest = dataB6[dataB6.index("|")+1:]
							student_id = rest[:rest.index("|")]
							#print(f"class name: {class_name}; student ID: {student_id}")
							return class_name, student_id
						except:
							return "Wrong data format"
			except:
				return "Hexa not valid"
				if command == "buzz1":
					ser.write(BUZZ1command) 
					#print(f"Done writing")
					in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
					print(f"hexa received: {in_hex}")

		if command == "buzz2":
			ser.write(BUZZ2command) 
			#print(f"Done writing")
			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			print(f"hexa received: {in_hex}")
			
		if command == "buzz3":
			ser.write(BUZZ3command) 
			#print(f"Done writing")
			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			print(f"hexa received: {in_hex}")
			
		if command == "led1":
			ser.write(LED1command) 
			#print(f"Done writing")
			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			print(f"hexa received: {in_hex}")
			
		if command == "led2":
			ser.write(LED2command) 
			#print(f"Done writing")
			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			print(f"hexa received: {in_hex}")
		if command == "buzz":
			ser.write(BUZZ2command)
			time.sleep(0.5)
			ser.write(BUZZ3command)
	

if __name__ == "__main__":
	main()