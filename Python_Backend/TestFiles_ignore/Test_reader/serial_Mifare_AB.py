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


# Command no.5.3.2.1
LOADKcommand = bytearray()
LOADKcommand.append(0xFF)   #CLA
LOADKcommand.append(0x82)   #INS
LOADKcommand.append(0x00)   #KEY STRUCTURE
LOADKcommand.append(0x00)   #KEY SLOT 4
LOADKcommand.append(0x06)   #KEY LENGTH
for i in range (6):
    LOADKcommand.append(0xFF)   #6 BYTE DATA

# Command no.5.3.2.2
AUTHcommand = bytearray()
AUTHcommand.append(0xFF)    #CLA
AUTHcommand.append(0x86)    #INS
AUTHcommand.append(0x00)    #P1
AUTHcommand.append(0x00)    #P2
AUTHcommand.append(0x05)    #LC
AUTHcommand.append(0x01)    #VERSION
AUTHcommand.append(0x00)    #ADDRESS MSB
AUTHcommand.append(0x04)    #BLOCK 4 AUTHENTICATED
AUTHcommand.append(0x60)    #KEY A
AUTHcommand.append(0x00)    #KEY NUMBER SLOT 0

# Command no.5.3.2.3
READB4command = bytearray()
READB4command.append(0xFF)  #CLA
READB4command.append(0xB0)  #INS
READB4command.append(0x00)  #MSB
READB4command.append(0x04)  #LSB
READB4command.append(0x10)  #LE

READB5command = bytearray()
READB5command.append(0xFF)  #CLA
READB5command.append(0xB0)  #INS
READB5command.append(0x00)  #MSB
READB5command.append(0x05)  #LSB
READB5command.append(0x10)  #LE

READB6command = bytearray()
READB6command.append(0xFF)  #CLA
READB6command.append(0xB0)  #INS
READB6command.append(0x00)  #MSB
READB6command.append(0x06)  #LSB
READB6command.append(0x10)  #LE

# Command no.5.3.2.4
UPDATEB4command = bytearray()
UPDATEB4command.append(0xFF)    #CLA
UPDATEB4command.append(0xD6)    #INS
UPDATEB4command.append(0x00)    #MSB
UPDATEB4command.append(0x04)    #LSB
UPDATEB4command.append(0x10)    #LC
    for i in range(16):
UPDATEB4command.append(0x00)    #DATA

UPDATEB5command = bytearray()
UPDATEB5command.append(0xFF)    #CLA
UPDATEB5command.append(0xD6)    #INS
UPDATEB5command.append(0x00)    #MSB
UPDATEB5command.append(0x05)    #LSB
UPDATEB5command.append(0x10)    #LC
    for i in range(16):
UPDATEB5command.append(0x00)    #DATA

UPDATEB6command = bytearray()
UPDATEB6command.append(0xFF)    #CLA
UPDATEB6command.append(0xD6)    #INS
UPDATEB6command.append(0x00)    #MSB
UPDATEB6command.append(0x06)    #LSB
UPDATEB6command.append(0x10)    #LC
    for i in range(16):
UPDATEB6command.append(0x00)    #DATA



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
                        "- rk4: read block 4 of Mifare card with Key included\n"
                        "- loadk:")

        if command == "rk4":
            ser.write(READKEY4command)
            # print(f"Done writing")

            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                # print("READ KEY command succeded")
                # print(f"hexaread {in_hex}")
                print(f"hexaread 2:9 {in_hex[2:9]}")
                # print(f"hexaread 17:-2 {in_hex[17:-2]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "loadk" :
            ser.write(LOADKcommand)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "AUTH":
            ser.write(AUTHcommand)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "READ4":
            ser.write(READB4command)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "READ5":
            ser.write(READB5command)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "READ6":
            ser.write(READB6command)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "UPDATEB4":
            ser.write(UPDATEB4command)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "UPDATEB5":
            ser.write(UPDATEB5command)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")

        if command == "UPDATEB6":
            ser.write(UPDATEB6command)
            in_hex = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            print(f"hexa received: {in_hex}")
            if in_hex[2:9] == '2001500':
                print(f"hexaread 2:9 {in_hex[2:9]}")
                data = str(codecs.decode(in_hex[17:-2], "hex"), 'utf-8')
                print(f"ASCII code: {data}")
	

if __name__ == "__main__":
	main()
