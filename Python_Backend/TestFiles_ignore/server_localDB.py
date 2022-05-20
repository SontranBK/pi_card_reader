#!/usr/bin/python
# 1A1
# 1083682100084


import sqlite3
import time
from datetime import datetime,date

# Decode the server response sent to our MCU
def decode_server_response(server_error_code, received_string, timeSentToUI):
	"""
	try:
		if (server_error_code == "00"):
			# Server response is saved in received string, this contains student information
			student_name = received_string["data"]["name"]
			student_id = received_string["data"]["studentId"]
			school_name = received_string["data"]["school"]["name"]
			class_name = received_string["data"]["clazz"]["name"]

			print(f'Information received from server: student_name_id: {student_name}, {student_id}\n'
					f'school_name: {school_name}\nclass_name: {class_name}\n')
			
			# Return body of UI message	
			return student_name + ' | ' + student_id + ' | '  + class_name + ' | ' + school_name + ' | ' + timeSentToUI + ' | ' + '000000000'
		else:
			return None
	except:
		return None
		print("Error: Server response's format is incorrect !!!!!!!!!\n")
	"""
	if (server_error_code == "00"):
			# Server response is saved in received string, this contains student information
			student_name = received_string["data"]["name"]
			student_id = received_string["data"]["studentId"]
			school_name = received_string["data"]["school"]["name"]
			class_name = received_string["data"]["clazz"]["name"]

			print(f'Information received from server: student_name_id: {student_name}, {student_id}\n'
					f'school_name: {school_name}\nclass_name: {class_name}\n')
			
			# Return body of UI message	
			return student_name + ' | ' + student_id + ' | '  + class_name + ' | ' + school_name + ' | ' + timeSentToUI + ' | ' + '000000000'
	else:
		return None

# Read data from database and update our local database
def read_database(connection, data, school_name_db, timeSentToUI):
	start = time.time()
	"""
	try:
		cursor = connection.execute(f"SELECT name from CLASS_{data[0]} where ID = {data[1]}")
		for row in cursor:
			print (f"\nFind student with following info:\nName = {row[0]}")
			pass				
		body = row[0] + ' | ' + data[1] + ' | '  + data[0] + ' | ' + school_name_db + ' | ' + timeSentToUI + ' | ' + '000000000'					
		end = time.time()
		print("Read local DB time: "+str(end-start))
		return body
	except:
		print("Error: Unable to read database !!!!!!!!!\n")
		end = time.time()
		print("Read local DB time: "+str(end-start))
		return None
	"""
	cursor = connection.execute(f"SELECT name from CLASS_{data[0]} where ID = {data[1]}")
	for row in cursor:
		print (f"\nFind student with following info:\nName = {row[0]}")
		pass				
	body = row[0] + ' | ' + data[1] + ' | '  + data[0] + ' | ' + school_name_db + ' | ' + timeSentToUI + ' | ' + '000000000'					
	end = time.time()
	print("Read local DB time: "+str(end-start))
	return body

# Read data from database and update our local database
def update_database(connection, data, server_error_code, timeSentToServer):
	try:
		cursor = connection.execute(f"SELECT time_a from CLASS_{data[0]} where ID = {data[1]}")
		for row in cursor:
			print (f"\nFind student with following info:\nTime A = {row[0]}")
			if (row[0] == None):
				connection.execute("UPDATE CLASS_{} set TIME_A = ? where ID = ?".format(data[0]),(timeSentToServer,data[1]))
				connection.execute("UPDATE CLASS_{} set ERROR_CODE_A = ? where ID = ?".format(server_error_code),(timeSentToServer,data[1]))
				connection.commit()
			else:
				connection.execute("UPDATE CLASS_{} set TIME_B = ? where ID = ?".format(data[0]),(timeSentToServer,data[1]))
				connection.execute("UPDATE CLASS_{} set ERROR_CODE_B = ? where ID = ?".format(server_error_code),(timeSentToServer,data[1]))
				connection.commit()			
	except:
		print("Error: Unable to update database !!!!!!!!!\n")

"""
# new ID list
ID_list =[str("0012-22-0219"),
str("0012-22-0006"),
str("0012-22-2157"),
str("0012-22-2558"),
str("0012-22-9059"),
str("0012-22-4304"),
str("0012-22-0150"),
str("0012-22-0985"),
str("0012-22-6907"),
str("0012-22-4748"),
str("0012-22-0181"),
str("0012-22-9096"),
]
"""
ID_list =[1083682100084, 1083682100100,
1083682100113,
1083682100111,
1083682100106,
1083682100089,
1083682100082,
1083682100077,
108368632000253,
1083682100109,
1083682100230,
1083682100076,
1083682100093,
]

input_class = "1A1"

# Define machine_id: id of our MCU device 
machine_id = "00001"
# Name of school where device is installed
school_name_db = "Tiểu học Thịnh Long"

database_link = None

for student_id in ID_list:

	# Modify the link to our database here
	# Sample name of database: 11_05_2022.db (format: day_month_year.db)

	data = []
	data.append(str(student_id))
	data.append(str("1A1"))
	print(f"our input data: {data[0]}, {data[1]}")

	try:
		#database_link = 'pi_card_reader/Database/Sample/SampleDB.db' # if you want to try out sample Database
		database_link = './pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db'
		#print(f"Link of database: {database_link}")
	except:
		print("Error: database link not found !!!!!!!!!\n")

	database_link = 'pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db'
	print(f"\n\nLink of database: {database_link}")
	conn = sqlite3.connect(database_link)

	print ("Opened database successfully\n")


	timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
	timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
	print(f"time sent to server: {timeSentToServer}")


	# Read student info from database if possible
	body = read_database(conn, data, school_name_db, timeSentToUI)
	print(f"Body read from local DB: {body}")
	postData = {
			"machineId": machine_id,
			"checkingTime": timeSentToServer,
			"studentID": data[1],}

	# Perform sending above request data to server and receive response
	try: 
		res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
		print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')

		received_string = json.loads(res.text)
	except:
		print("Error: Lost connection to OCD server !!!!!!!!!\n")
		received_string = {"errorCode":"","errorMessage":""}

	# Error code of server response	
	server_error_code = received_string["errorCode"]
	print(f"Server response error code: {server_error_code}")

	# What to do with our information? 
	# 1) Send to server and receive response data
	# OR 2) Look this information up in our local database and update database
	# OR 3) Do both of above

	# Update Time A or Time B in local database
	update_database(conn, data, server_error_code, timeSentToServer)

	# If our local database doesn't work, turn into server response and decode it for information
	if body == None:
		# If we're unable to decode server's response, body will be none
		# Then, mission fail. Studen information is not valid
		body = decode_server_response(server_error_code, received_string, timeSentToUI)
		print(f"Body read from server: {body}")
	time.sleep(15)


	
