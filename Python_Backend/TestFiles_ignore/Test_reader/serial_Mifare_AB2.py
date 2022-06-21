#!/usr/bin/python3

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



def main():
    r = readers()
    print (readers())
    connection = r[0].createConnection()
    connection.connect()

    #SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
    #DF_TELECOM = [0x7F, 0x10]
    #card_response = connection.transmit( SELECT + DF_TELECOM )
    #print(card_response)


if __name__ == "__main__":
	main()
