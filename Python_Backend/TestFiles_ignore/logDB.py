
import sqlite3
import time
from datetime import datetime,date
from requests import Session
import json



server = 'http://171.244.207.65:7856'


ses = Session()
ses.headers.update({
    'Content-Type': 'application/json'
})
ID_list =[
str("0101-22-9042"),
str("0101-22-6342"),
str("0101-22-2379"),
str("0101-22-1758"),
str("0101-22-8388"),
str("0101-22-8078"),
str("0101-22-3406"),
]


input_class = "1A1"

# Define machine_id: id of our MCU device 
machine_id = "00001"



while(True):
	for student_id in ID_list:

		# Modify the link to our database here
		# Sample name of database: 11_05_2022.db (format: day_month_year.db)

		data = []
		data.append(str("1A1"))
		data.append(str(student_id))
		#print(f"our input data: {data[0]}, {data[1]}")
		timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
		postData = {
			"machineId": machine_id,
			"checkingTime": timeSentToServer,
			"studentID": data[1],}

		try: 
			res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
			print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')

			received_string = json.loads(res.text)
		except:
			print("Error: Lost connection to OCD server !!!!!!!!!\n")
			received_string = {"errorCode":"","errorMessage":""}
			try: 
				conn = sqlite3.connect("log_retry.db")
				conn.cursor().execute("CREATE TABLE IF NOT EXISTS LOGTABLE( machineID TEXT, checkingTime TEXT, studentID TEXT, retryTimes TEXT) ")
				conn.execute("INSERT INTO LOGTABLE (machineID,checkingTime,studentID,retryTimes) VALUES (?,?,?,?)",(machine_id,timeSentToServer,data[1],0))
				conn.commit()
			except: 
				pass

		"""
		try: 
			conn = sqlite3.connect("log_retry.db")
			conn.cursor().execute("CREATE TABLE IF NOT EXISTS LOGTABLE( machineID TEXT, checkingTime TEXT, studentID TEXT, retryTimes TEXT) ")

			conn.execute("INSERT INTO LOGTABLE (machineID,checkingTime,studentID,retryTimes) VALUES (?,?,?,?)",(request['machineID'],request['checkingTime'],request['studentID'],0))
			conn.commit()
		except:
			pass
		"""
		time.sleep(1)

