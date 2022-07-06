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

                READ4 = [0xFF, 0xb0, 0x00, 0x04, 0x10]
                card_response = connection.transmit(READ4)
                #print(f"read4 res: if sw1 is 144 then is correct: {card_response}")
                #print(type(card_response[0]))
                DATA4 = card_response[0]
                if card_response[1] == 144:
                    READ5 = [0xFF, 0xb0, 0x00, 0x05, 0x10]
                    card_response = connection.transmit(READ5)
                    #print(f"read5 res: if sw1 is 144 then is correct: {card_response}")
                    DATA5 = card_response[0]
                    if card_response[1] == 144:
                        READ6 = [0xFF, 0xb0, 0x00, 0x06, 0x10]
                        card_response = connection.transmit(READ6)
                        #print(f"read6 res: if sw1 is 144 then is correct: {card_response}")
                        DATA6 = card_response[0]
                        if card_response[1] == 144:
                            DATA = DATA4 + DATA5 + DATA6
                            #print(type(DATA[0]))
                            DATA0 = []
                            for i in range (0,47,1):
                                DATA0.append(chr(DATA[i]))
                            #print(DATA0)
                            strDATA = "".join(DATA0)
                            print(strDATA)
                            BUZZ = [0xFF, 0x00, 0x04, 0x01, 0x03, 0x19, 0x19, 0x02]
                            card_response = connection.transmit(BUZZ)
                            #print(f"write res: if sw1 is 144 then is correct: {card_response}")
            except:
                print("cant read data")
        time.sleep(1.5)

if __name__ == "__main__":
    main()

