#!/usr/bin/python3
# https://pyscard.sourceforge.io/#documentation
# sudo python3 serial_Mifare_AB2.py

"""
This is a serial Mifare AB Circle python code
"""

import sys
import time
sys.path.append('./.local/lib/python3.9/site-packages')
from smartcard.System import readers
from smartcard.util import toHexString
import time
from datetime import datetime,date
import codecs
import re
card_present = False
def main():
    r = readers()
    print (readers())
    # ['Circle CIR315 [CIR315 PICC] 00 00', 'Circle CIR315 [CIR315 SAM] 01 00'] -> CIR315A -> connection = r[0].createConnection()
    # ['Circle CIR315 Dual & 1S [CIR315 Dual & 1S] 00 00', 'Circle CIR315 Dual & 1S [CIR315 Dual & 1S] 00 01', 'Circle CIR315 Dual & 1S [CIR315 Dual & 1S] 00 02'] -> CIR315B -> connection = r[1].createConnection()
    while(True):
        try:
            connection = r[0].createConnection()
            #print(connection)
            connection.connect()
            card_present = True
        except:
            card_present = False
            print("no card found")
        if card_present == True:
            try:
                LOADKEY = [0xFF, 0x82, 0x00, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                card_response = connection.transmit(LOADKEY)
                #print(f"loadkey res: if sw1 is 144 then is correct: {card_response}")

                AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x04, 0x60, 0x00]
                card_response = connection.transmit(AUTH)
                #print(f"auth res: if sw1 is 144 then is correct: {card_response[2]}")

                Lop = input("Nhap lop: \n")
                Mahocsinh = input("Nhap ma hoc sinh: \n")
                Ten = input ("Nhap ten: \n")
                inp = Lop + "" + "|" + "" + Mahocsinh + "" + "|" + "" + Ten
                Data = inp.encode('utf-8')
                Hex_Data = Data.hex()
                list_hex = re.split("(\w\w)", Hex_Data[:])[1::2]
                for i in range(48 - len(list_hex)):
                    list_hex.append('00')
                for i in range(48):
                    # if i == 0:
                    # list_hex[i] = '00'
                    list_hex[i] = '0x' + list_hex[i]
                print(list_hex)

                print("Now write block 4")
                WRITE4 = [0xFF, 0xD6, 0x00, 0x04, 0x10, int(list_hex[0], 16), int(list_hex[1], 16),
                          int(list_hex[2], 16), int(list_hex[3], 16), int(list_hex[4], 16), int(list_hex[5], 16),
                          int(list_hex[6], 16), int(list_hex[7], 16), int(list_hex[8], 16), int(list_hex[9], 16),
                          int(list_hex[10], 16), int(list_hex[11], 16), int(list_hex[12], 16), int(list_hex[13], 16),
                          int(list_hex[14], 16), int(list_hex[15], 16)]
                card_response = connection.transmit(WRITE4)
                #print(card_response[1])
                if card_response[1] == 144:
                    print("Now write block 5")
                    WRITE5 = [0xFF, 0xD6, 0x00, 0x05, 0x10, int(list_hex[16], 16), int(list_hex[17], 16),
                                  int(list_hex[18], 16), int(list_hex[19], 16), int(list_hex[20], 16), int(list_hex[21], 16),
                                  int(list_hex[22], 16), int(list_hex[23], 16), int(list_hex[24], 16), int(list_hex[25], 16),
                                  int(list_hex[26], 16), int(list_hex[27], 16), int(list_hex[28], 16), int(list_hex[29], 16),
                                  int(list_hex[30], 16), int(list_hex[31], 16)]
                    card_response = connection.transmit(WRITE5)
                    if card_response[1] == 144:
                        print("Now write block 6")
                        WRITE6 = [0xFF, 0xD6, 0x00, 0x06, 0x10, int(list_hex[32], 16), int(list_hex[33], 16),
                                          int(list_hex[34], 16), int(list_hex[35], 16), int(list_hex[36], 16), int(list_hex[37], 16),
                                          int(list_hex[38], 16), int(list_hex[39], 16), int(list_hex[40], 16), int(list_hex[41], 16),
                                          int(list_hex[42], 16), int(list_hex[43], 16), int(list_hex[44], 16), int(list_hex[45], 16),
                                          int(list_hex[46], 16), int(list_hex[47], 16)]
                        card_response = connection.transmit(WRITE6)
                        BUZZ = [0xFF, 0x00, 0x04, 0x01, 0x03, 0x19, 0x19, 0x02]
                        card_response = connection.transmit(BUZZ)
                        # print(f"write res: if sw1 is 144 then is correct: {card_response}")
                        print("Write complete")
            except:
                print("Cant write data")

        time.sleep(3)

if __name__ == "__main__":
    main()

