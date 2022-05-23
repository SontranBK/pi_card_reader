#!/usr/bin/python3
 
"""
This is a serial Mifare DU-950 python code
for reading block 4,5,6 continuously
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

		if command == "rk4":
			ser.write(READKEY4command) 
			#print(f"Done writing")


			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			print(f"hexa received: {in_hex}")
			if in_hex[2:9] == '2001500':
				#print("READ KEY command succeded")
				#print(f"hexaread {in_hex}")
				print(f"hexaread 2:9 {in_hex[2:9]}")
				#print(f"hexaread 17:-2 {in_hex[17:-2]}")
				data = str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')
				print(f"ASCII code: {data}")
			
		

	

if __name__ == "__main__":
	main()
 

