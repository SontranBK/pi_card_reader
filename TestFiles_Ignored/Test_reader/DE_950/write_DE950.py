import sys
import time

sys.path.append('./.local/lib/python3.9/site-packages')
import serial
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
# Command no.38 for Block 4
lop= input("Nhap lop: \n")
mssv= input("Nhap ma hoc sinh: \n")
name= input("Nhap ten hoc sinh: \n")
inp= lop + '' + "|" + '' + mssv + '' + '|' + name
Data=inp.encode('utf-8')
Hex_Data=Data.hex()
list_hex = re.split("(\w\w)", Hex_Data[:])[1::2]
for i in range(48-len(list_hex)):
    list_hex.append('00')
for i in range(48):
    #if i == 0:
        #list_hex[i] = '00'
    list_hex[i] = '0x'+ list_hex[i]
#print(list_hex)
    #CaculateXOR
lenl = 0x1a
cmd = 0x38
block4 = 0x04
block5 = 0x05
block6 = 0x06
result = int(list_hex[0],16) ^ int(list_hex[1],16)

for i in range(2,16,1):
    result = int(list_hex[i], 16) ^ result

result = int(lenl) ^ result
result = int(cmd) ^ result
result = int(block4) ^ result

result2 = int(list_hex[16],16) ^ int(list_hex[17],16)

for i in range(18,32,1):
    result2 = int(list_hex[i], 16) ^ result2
result2 = int(lenl) ^ result2
result2 = int(cmd) ^ result2
result2 = int(block5) ^ result2

result3 = int(list_hex[32],16) ^ int(list_hex[33],16)

for i in range(34,48,1):
    result3 = int(list_hex[i], 16) ^ result3

result3 = int(lenl) ^ result3
result3 = int(cmd) ^ result3
result3 = int(block6) ^ result3

WRITEKEY4command = bytearray()
WRITEKEY4command.append(0x02)  # STX
WRITEKEY4command.append(0x00)  # LEN-H
WRITEKEY4command.append(0x1A)  # LEN-L
WRITEKEY4command.append(0x38)  # CMD
WRITEKEY4command.append(0x00)  # R-Mode
WRITEKEY4command.append(0x00)  # A-Mode
WRITEKEY4command.append(0x04)  # Block 4
for i in range(6):  # Key0-5
    WRITEKEY4command.append(0xFF)
WRITEKEY4command.append(int(list_hex[0],16))  # Data 0-15
WRITEKEY4command.append(int(list_hex[1],16))
WRITEKEY4command.append(int(list_hex[2],16))
WRITEKEY4command.append(int(list_hex[3],16))
WRITEKEY4command.append(int(list_hex[4],16))
WRITEKEY4command.append(int(list_hex[5],16))
WRITEKEY4command.append(int(list_hex[6],16))
WRITEKEY4command.append(int(list_hex[7],16))
WRITEKEY4command.append(int(list_hex[8],16))
WRITEKEY4command.append(int(list_hex[9],16))
WRITEKEY4command.append(int(list_hex[10],16))
WRITEKEY4command.append(int(list_hex[11],16))
WRITEKEY4command.append(int(list_hex[12],16))
WRITEKEY4command.append(int(list_hex[13],16))
WRITEKEY4command.append(int(list_hex[14],16))
WRITEKEY4command.append(int(list_hex[15],16))
WRITEKEY4command.append(result)  # LRC

# Command no.38 for Block 5
WRITEKEY5command = bytearray()
WRITEKEY5command.append(0x02)  # STX
WRITEKEY5command.append(0x00)  # LEN-H
WRITEKEY5command.append(0x1A)  # LEN-L
WRITEKEY5command.append(0x38)  # CMD
WRITEKEY5command.append(0x00)  # R-Mode
WRITEKEY5command.append(0x00)  # A-Mode
WRITEKEY5command.append(0x05)  # Block 5
for i in range(6):  # Key0-5
    WRITEKEY5command.append(0xFF)
WRITEKEY5command.append(int(list_hex[16],16))  # Data 0-15
WRITEKEY5command.append(int(list_hex[17],16))
WRITEKEY5command.append(int(list_hex[18],16))
WRITEKEY5command.append(int(list_hex[19],16))
WRITEKEY5command.append(int(list_hex[20],16))
WRITEKEY5command.append(int(list_hex[21],16))
WRITEKEY5command.append(int(list_hex[22],16))
WRITEKEY5command.append(int(list_hex[23],16))
WRITEKEY5command.append(int(list_hex[24],16))
WRITEKEY5command.append(int(list_hex[25],16))
WRITEKEY5command.append(int(list_hex[26],16))
WRITEKEY5command.append(int(list_hex[27],16))
WRITEKEY5command.append(int(list_hex[28],16))
WRITEKEY5command.append(int(list_hex[29],16))
WRITEKEY5command.append(int(list_hex[30],16))
WRITEKEY5command.append(int(list_hex[31],16))
WRITEKEY5command.append(result2)  # LRC

# Command no.38 for Block 6
WRITEKEY6command = bytearray()
WRITEKEY6command.append(0x02)  # STX
WRITEKEY6command.append(0x00)  # LEN-H
WRITEKEY6command.append(0x1A)  # LEN-L
WRITEKEY6command.append(0x38)  # CMD
WRITEKEY6command.append(0x00)  # R-Mode
WRITEKEY6command.append(0x00)  # A-Mode
WRITEKEY6command.append(0x06)  # Block 6
for i in range(6):  # Key0-5
    WRITEKEY6command.append(0xFF)
WRITEKEY6command.append(int(list_hex[32],16))  # Data 0-15
WRITEKEY6command.append(int(list_hex[33],16))
WRITEKEY6command.append(int(list_hex[34],16))
WRITEKEY6command.append(int(list_hex[35],16))
WRITEKEY6command.append(int(list_hex[36],16))
WRITEKEY6command.append(int(list_hex[37],16))
WRITEKEY6command.append(int(list_hex[38],16))
WRITEKEY6command.append(int(list_hex[39],16))
WRITEKEY6command.append(int(list_hex[40],16))
WRITEKEY6command.append(int(list_hex[41],16))
WRITEKEY6command.append(int(list_hex[42],16))
WRITEKEY6command.append(int(list_hex[43],16))
WRITEKEY6command.append(int(list_hex[44],16))
WRITEKEY6command.append(int(list_hex[45],16))
WRITEKEY6command.append(int(list_hex[46],16))
WRITEKEY6command.append(int(list_hex[47],16))
WRITEKEY6command.append(result3)  # LRC

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
        # inp = input("Nhap du lieu: \n").encode('utf-8')
        if command == "writekey":
            ser.write(WRITEKEY4command)
            print("Now write key 4")
            in_hexB4 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
            #print(f"list hex B4 {in_hexB4}")
            #print(f"command4 {WRITEKEY4command}")
            #print(in_hexB4[2:9])
            if in_hexB4[2:9] == '2000500':
                print("Now write key 5")
                ser.write(WRITEKEY5command)
                in_hexB5 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                #print(f"list hex {in_hexB5}")
                if in_hexB5[2:9] == '2000500':
                    print("Now write key 6")
                    ser.write(WRITEKEY6command)
                    in_hexB6 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                    if in_hexB6[2:9] == '2000500':
                        ser.write(BUZZ2command)
                        time.sleep(0.15)
                        ser.write(BUZZ3command)

if __name__ == "__main__":
    main()