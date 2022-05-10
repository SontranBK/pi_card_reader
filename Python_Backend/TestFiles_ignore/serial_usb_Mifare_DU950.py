#!/usr/bin/python3
 
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

		ser.write(READKEY4command) 
		#print(f"Done writing")


		in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
		#print(f"hexa received: {in_hex}")
		if in_hex[2:9] == '2001500':
			#print("READ KEY command succeded")
			#print(f"hexaread {in_hex}")
			#print(f"hexaread 2:9 {in_hex[2:9]}")
			#print(f"hexaread 17:-2 {in_hex[17:-2]}")
			data = str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')
			#print(f"ASCII code: {data}")
			
			ser.write(READKEY5command)
			
			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			#print(f"hexa received: {in_hex}")
			if in_hex[2:9] == '2001500':
				#print("READ KEY command succeded")
				#print(f"hexaread {in_hex}")
				#print(f"hexaread 2:9 {in_hex[2:9]}")
				#print(f"hexaread 17:-2 {in_hex[17:-2]}")
				data = data + str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')
				#print(f"ASCII code: {data}")
				
				ser.write(READKEY6command)
			
				in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
				#print(f"hexa received: {in_hex}")
				if in_hex[2:9] == '2001500':
					#print("READ KEY command succeded")
					#print(f"hexaread {in_hex}")
					#print(f"hexaread 2:9 {in_hex[2:9]}")
					#print(f"hexaread 17:-2 {in_hex[17:-2]}")
					data = data + str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')
					print(f"ASCII code: {data}")
			
			
		

	

if __name__ == "__main__":
	main()
 

