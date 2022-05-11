#!/usr/bin/python
# 1A1
# 1083682100084

import sqlite3
import time
from datetime import datetime,date

# Modify the link to our database here
# Sample name of database: 11_05_2022.db (format: day_month_year)
database_link = 'DB thg5/'+ date.today().strftime('%d_%m_%Y') +'.db'

print(f"Link of database: {database_link}")
conn = sqlite3.connect(database_link)

print ("Opened database successfully\n")

while(True):
	inputClass = input("Input Class: ")
	inputID = input("Input ID: ")
	timeSentToServer = date.today().strftime('%Y-%m-%d')
	print(f"time sent to server: {timeSentToServer}")
	start = time.time()

	cursor = conn.execute(f"SELECT name, id, dateofbirth, time_a, error_code_a, time_b, error_code_b from CLASS_{inputClass} where ID = {inputID}")
	for row in cursor:
		print (f"\nFind student with following info:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
		if (row[3] == None):
			#row[3] = timeSentToServer
			conn.execute(f"UPDATE CLASS_{inputClass} set TIME_A = {timeSentToServer} where ID = {inputID}")
			conn.commit()
			print (f"After updating time:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
		else:
			#row[5] = timeSentToServer
			conn.execute(f"UPDATE CLASS_{inputClass} set TIME_B = {timeSentToServer} where ID = {inputID}")
			conn.commit()
			print (f"After updating time:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
	end = time.time()
	print("Execution time: "+str(end-start))
	

conn.close()
