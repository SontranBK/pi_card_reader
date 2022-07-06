import serial
import sys
import time
from datetime import datetime, date
import codecs
import re

BUZZ2command = bytearray()
BUZZ2command.append(0x02)  # STX
BUZZ2command.append(0x00)  # LEN-H
BUZZ2command.append(0x02)  # LEN-L
BUZZ2command.append(0x13)  # BUZZ2 CMD
BUZZ2command.append(0x00)  # BUZZ2 On
BUZZ2command.append(0x11)  # LRC

BUZZ3command = bytearray()
BUZZ3command.append(0x02)  # STX
BUZZ3command.append(0x00)  # LEN-H
BUZZ3command.append(0x02)  # LEN-L
BUZZ3command.append(0x13)  # BUZZ3 CMD
BUZZ3command.append(0x01)  # BUZZ3 Off
BUZZ3command.append(0x10)  # LRC
# Command no.36 for block 4
READKEY4command = bytearray()
READKEY4command.append(0x02)  # STX
READKEY4command.append(0x00)  # LEN-H
READKEY4command.append(0x0A)  # LEN-L
READKEY4command.append(0x36)  # REQA CMD
READKEY4command.append(0x00)  # R mode
READKEY4command.append(0x00)  # A mode
READKEY4command.append(0x04)  # Block number of the card
for i in range(6):
    READKEY4command.append(0xFF)  # Key[0]..[5], The key data to be stored into the secret key buffer
READKEY4command.append(0x38)  # LRC

# Command no.36 for block 5
READKEY5command = bytearray()
READKEY5command.append(0x02)  # STX
READKEY5command.append(0x00)  # LEN-H
READKEY5command.append(0x0A)  # LEN-L
READKEY5command.append(0x36)  # REQA CMD
READKEY5command.append(0x00)  # R mode
READKEY5command.append(0x00)  # A mode
READKEY5command.append(0x05)  # Block number of the card
for i in range(6):
    READKEY5command.append(0xFF)  # Key[0]..[5], The key data to be stored into the secret key buffer
READKEY5command.append(0x39)  # LRC

# Command no.36 for block 6
READKEY6command = bytearray()
READKEY6command.append(0x02)  # STX
READKEY6command.append(0x00)  # LEN-H
READKEY6command.append(0x0A)  # LEN-L
READKEY6command.append(0x36)  # REQA CMD
READKEY6command.append(0x00)  # R mode
READKEY6command.append(0x00)  # A mode
READKEY6command.append(0x06)  # Block number of the card
for i in range(6):
    READKEY6command.append(0xFF)  # Key[0]..[5], The key data to be stored into the secret key buffer
READKEY6command.append(0x3a)  # LRC
def main():
    # initialize serial python, framework for reading serial USB
    ser = serial.Serial(
        port="COM3",
        baudrate=115200,
        timeout=0.05)

    # print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")
    while (True):
        command = input("Please insert 1 of following commands:\n"
                        "- rk4: read block 4 of Mifare card with Key included\n")
        if command == "readkey":
            try:
                dataB4 = ""
                dataB5 = ""
                dataB6 = ""
                ser.write(READKEY4command)
                in_hexB4 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                print(in_hexB4)
                print (in_hexB4[2:9])
                if in_hexB4[2:9] == '2001500':
                    dataB4 = str(codecs.decode(in_hexB4[17:49], "hex"), 'utf-8')
                    ser.write(READKEY5command)
                    in_hexB5 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                    if in_hexB5[2:9] == '2001500':
                        dataB5 = dataB4 + str(codecs.decode(in_hexB5[17:49], "hex"), 'utf-8')
                        ser.write(READKEY6command)
                        in_hexB6 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                        if in_hexB6[2:9] == '2001500':
                            dataB6 = dataB5 + str(codecs.decode(in_hexB6[17:49], "hex"), 'utf-8')
                            print(f"data: {dataB6}")
                            ser.write(BUZZ2command)
                            time.sleep(0.15)
                            ser.write(BUZZ3command)
                        try:
                            class_name = dataB6[:dataB6.index("|")]
                            rest = dataB6[dataB6.index("|") + 1:]
                            student_id = rest[:rest.index("|")]
                            # print(f"class name: {class_name}; student ID: {student_id}")
                            return class_name, student_id
                        except:
                            return "Wrong data format"
            except:
                return "Hexa not valid"
if __name__ == "__main__":
    main()