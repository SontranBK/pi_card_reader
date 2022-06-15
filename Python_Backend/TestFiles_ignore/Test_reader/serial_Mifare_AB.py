#!/usr/bin/python3

# sudo python3 serial_Mifare_AB.py 

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
		port = "/dev/ttyAMA0",
		baudrate = 115200,
		timeout = 0.05)
	

	print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")
	"""
	Check out protocol Duali file for protocol information
	All command below must have STX and LRC in font and back
	Read "Communication Protocol Frame Format" in page 9 for STX and LRC information
	"""
	# read USB serial and convert to string
	# Command no.21
	
	
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
