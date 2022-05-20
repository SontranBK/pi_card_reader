#!/usr/bin/python
# 1A1
# 1083682100084

import sqlite3
import time
from datetime import datetime,date

school_name_db = "Tiểu học Thịnh Long"

database_link = None

while(True):

	inputClass = input("\n\n\nInput Class: ")
	#inputID = input("Input ID: ")
	#inputClass ='1A1'
	inputID = '1083682100084'


	#data[0] = inputClass
	#data[1] = inputID

	# Modify the link to our database here
	# Sample name of database: 11_05_2022.db (format: day_month_year.db)

	if (database_link != 'pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db'):
		database_link = 'pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db''
		print(f"\n\nLink of database: {database_link}")
		conn = sqlite3.connect(database_link)

	print ("Opened database successfully\n")


	timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
	timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
	print(f"time sent to server: {timeSentToServer}")

	start = time.time()

	cursor = conn.execute(f"SELECT name, time_a from CLASS_{inputClass} where ID = {inputID}")
	for row in cursor:
		print (f"\nFind student with following info:\nName = {row[0]}\nTime A = {row[1]}")
		if (row[1] == None):
			conn.execute("UPDATE CLASS_{} set TIME_A = ? where ID = ?".format(inputClass),(timeSentToServer,inputID))
			conn.commit()
		else:
			conn.execute("UPDATE CLASS_{} set TIME_B = ? where ID = ?".format(inputClass),(timeSentToServer,inputID))
			conn.commit()
	
	
	body = row[0] + ' | ' + inputID + ' | '  + inputClass + ' | ' + school_name_db + ' | ' + timeSentToUI + ' | ' + '000000000'
	print(f"Info sent to UI:{body}")

	end = time.time()
	print("Execution time: "+str(end-start))
	
