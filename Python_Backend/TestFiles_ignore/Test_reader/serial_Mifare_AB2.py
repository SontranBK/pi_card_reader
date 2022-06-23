#!/usr/bin/python3
# https://pyscard.sourceforge.io/#documentation
# sudo python3 serial_Mifare_AB2.py 

"""
This is a serial Mifare AB Circle python code
"""

import sys
import time
#sys.path.append('./.local/lib/python3.9/site-packages')
from smartcard.System import readers
from smartcard.util import toHexString
import time
from datetime import datetime,date
import codecs



def main():
    r = readers()
    print (r)
    connection = r[1].createConnection()
    connection.connect()

    # ([], 144, 0), this is correct response
    # Since 144 decimal is 0x90 hexa, 0 decimal is 0x00 hexa

    # ([], 99, 0), this is not correct response
    # Scine 99 decimal is 0x63 hexa, 0 decimal is 0x00 hexa

    
    """
    LOADKEY = [0xFF, 0x82, 0x00, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    card_response = connection.transmit(LOADKEY)
    print(f"loadkey res: if sw1 is 144 then is correct: {card_response}")
    
    AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x04, 0x60, 0x00]
    card_response = connection.transmit(AUTH)
    print(f"auth res: if sw1 is 144 then is correct: {card_response}")
    
    WRITE4 = [0xFF, 0xD6, 0x00, 0x04, 0x10, 0x31, 0x41, 0x31, 0x7c, 0x31, 0x30, 0x38, 0x33, 0x36, 0x38, 0x36, 0x33, 0x32, 0x30, 0x30, 0x30]
    card_response = connection.transmit(WRITE4)
    print(f"write res: if sw1 is 144 then is correct: {card_response}")
    """
    
    BUZZ = [0xFF, 0x00, 0x04, 0x01, 0x03, 0x19, 0x19, 0x02]
    card_response = connection.transmit(BUZZ)
    print(f"write res: if sw1 is 144 then is correct: {card_response}")


if __name__ == "__main__":
	main()