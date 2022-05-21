# flutter run -d web-server --web-hostname 127.0.0.1 --web-port 8989
#!/usr/bin/python3

import sys
sys.path.append('./.local/lib/python3.9/site-packages')
import codecs
import time
import serial
from requests import Session
import time
from datetime import datetime,date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import sqlite3
import json


"""
SECTION 1: DEFINE VARIABLES AND COMMAND
"""
# Define machine_id: id of our MCU device 
machine_id = "00001"
# Name of school where device is installed
school_name_db = "Tiểu học Thịnh Long"

database_link = None

# READKEY command of DU950 reader
# Please refer to our provided protocol

# READKEY command applied to block no.4
READKEY4command = bytearray()
READKEY4command.append(0x02) # STX
READKEY4command.append(0x00) # LEN-H
READKEY4command.append(0x0A) # LEN-L
READKEY4command.append(0x36) # REQA CMD
READKEY4command.append(0x00) # R mode
READKEY4command.append(0x00) # A mode
READKEY4command.append(0x04) # Block number of the card
for i in range(6):
	READKEY4command.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
READKEY4command.append(0x38) # LRC

# READKEY command applied to block no.5
READKEY5command = bytearray()
READKEY5command.append(0x02) # STX
READKEY5command.append(0x00) # LEN-H
READKEY5command.append(0x0A) # LEN-L
READKEY5command.append(0x36) # REQA CMD
READKEY5command.append(0x00) # R mode
READKEY5command.append(0x00) # A mode
READKEY5command.append(0x05) # Block number of the card
for i in range(6):
	READKEY5command.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
READKEY5command.append(0x39) # LRC

# READKEY command applied to block no.6
READKEY6command = bytearray()
READKEY6command.append(0x02) # STX
READKEY6command.append(0x00) # LEN-H
READKEY6command.append(0x0A) # LEN-L
READKEY6command.append(0x36) # REQA CMD
READKEY6command.append(0x00) # R mode
READKEY6command.append(0x00) # A mode
READKEY6command.append(0x06) # Block number of the card
for i in range(6):
	READKEY6command.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
READKEY6command.append(0x3a) # LRC

"""
SECTION 2: FUNCTION DEFINATION
"""

# Decode the server response sent to our MCU
def decode_server_response(server_error_code, received_string, timeSentToUI):
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

# Read data from database and update our local database
def read_database(connection, data, school_name_db, timeSentToUI):
	try:
		cursor = connection.execute(f"SELECT name from CLASS_{data[0]} where ID = {data[1]}")
		for row in cursor:
			print (f"\nFind student with following info:\nName = {row[0]}")
			pass				
		body = row[0] + ' | ' + data[1] + ' | '  + data[0] + ' | ' + school_name_db + ' | ' + timeSentToUI + ' | ' + '000000000'
		return body
	except:
		print("Error: Unable to read database !!!!!!!!!\n")
		return None

# Read data from database and update our local database
def update_database(connection, data, timeSentToServer):
	try:
		cursor = connection.execute(f"SELECT time_a from CLASS_{data[0]} where ID = {data[1]}")
		for row in cursor:
			print (f"\nFind student with following info:\nTime A = {row[0]}")
			if (row[0] == None):
				connection.execute("UPDATE CLASS_{} set TIME_A = ? where ID = ?".format(data[0]),(timeSentToServer,data[1]))
				connection.commit()
			else:
				connection.execute("UPDATE CLASS_{} set TIME_B = ? where ID = ?".format(data[0]),(timeSentToServer,data[1]))
				connection.commit()			
	except:
		print("Error: Unable to update database !!!!!!!!!\n")
		

# Read data from our NFC reader by sending READKEY command
def read_NFC_card(ser):
	dataB4 = ""
	dataB5 = ""
	dataB6 = ""
	ser.write(READKEY4command) 
	in_hexB4 = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
	if in_hexB4[2:9] == '2001500':
		dataB4 = str(codecs.decode(in_hexB4[17:49], "hex"),'utf-8')		
		ser.write(READKEY5command)
		in_hexB5 = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
		if in_hexB5[2:9] == '2001500':
			dataB5 = dataB4 + str(codecs.decode(in_hexB5[17:49], "hex"),'utf-8')			
			ser.write(READKEY6command)		
			in_hexB6 = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			if in_hexB6[2:9] == '2001500':
				dataB6 = dataB5 + str(codecs.decode(in_hexB6[17:49], "hex"),'utf-8')	
				print(f"data: {dataB6}")
			try:
				class_name = dataB6[:dataB6.index("|")]
				rest = dataB6[dataB6.index("|")+1:]
				student_id = rest[:rest.index("|")]
				print(f"class name: {class_name}; student ID: {student_id}")
				return class_name, student_id
			except:
				pass
				
# Send data from python code (backend) to UI (fontend)
def send_all(title,body,FCM_token):
	try:
		# [START send_all]
		# Create a list containing up to 500 messages.
		messages = [
		messaging.Message(
			notification=messaging.Notification(title, body),
			token=FCM_token,
		),

		]

		response = messaging.send_all(messages)
		# See the BatchResponse reference documentation
		# for the contents of response.
		print('{0} messages were sent successfully'.format(response.success_count))
		# [END send_all]
	except:
		print("Error: Unable to connect with UI !!!!!!!!!\n")



"""
SECTION 3: MAIN PROGRAM
"""


def main():
	# Initialize firebase, API for backend-UI communication
	cred = credentials.Certificate('service-account.json')
	default_app = firebase_admin.initialize_app(cred)

	# Initialize API for connecting to server-backend
	server = 'http://171.244.207.65:7856'
	ses = Session()
	ses.headers.update({
		'Content-Type': 'application/json'})
	
	# Initialize firebase TOKEN API
	try: 
		with open('/home/metaedu/Downloads/API_TOKEN.txt') as f:
			MY_TOKEN = f.read()
		print (f"Token received form file: {MY_TOKEN}, type: {type({MY_TOKEN})}")
	except:
		print("Error: UI Token not found !!!!!!!!!\n")
		MY_TOKEN = 'c7y9di1Dwje8TXegJiyBZX:APA91bH-SZpjbjx2YWl0MSMb4FIkSIvzbncn7PQjHUvcqaKdNPFrv9YdcJvEffdB4DUDe5l4ip1DO88o4Du9xinaWTubXWUXGsW-G8Qn36S6WJJ5LJ8i64Wdj-CxVuEFHdNWfo8t_Oj1'
	
	# Initialize our local database
	try:
		database_link = 'pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db'
		#print(f"Link of database: {database_link}")
		conn = sqlite3.connect(database_link)
	except:
		database_link = 'pi_card_reader/Database/Sample/SampleDB.db'
		print(f"\n\nLink of database: {database_link}")
		conn = sqlite3.connect(database_link)

		print("Error: database link not found, could not connect to local DB !!!!!!!!!\n")
		print("Error: connect to Sample DB instead !!!!!!!!!\n")


	# Initialize serial python, framework for reading serial USB
	try:
		ser = serial.Serial(
			port = "/dev/ttyUSB0",
			baudrate = 115200,
			timeout = 0.05)
		print("Start reading !!!!!!!!!\n")
		send_all('Start: Start using NFC reader',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m') + '; ID thiet bi: ' + machine_id,MY_TOKEN) # send infomation to User interface
	except: 
		print ('Error: Reader not connected')
		send_all('Error: Reader not connected',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN) # send infomation to User interface
	
	# MAIN LOOP
	while (True): 
		# Read data from NFC reader
		# data[0] is class name, data[1] is student ID
		data = read_NFC_card(ser)
		#print(f"Received data: {data}")

		# If NFC card is presented and NFC reader return data
		if data != None:
					
			# We first look this information up in our local database and update database
			# If our local database somehow doesn't work, body will be none. Then we count on server's response
			if (database_link != 'pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db'):
				try:
					database_link = 'pi_card_reader/Database/Local_database/'+ date.today().strftime('%d_%m_%Y') +'.db'
					print(f"\n\nLink of database: {database_link}")
					conn = sqlite3.connect(database_link)
				except:
					database_link = 'pi_card_reader/Database/Sample/SampleDB.db'
					print(f"\n\nLink of database: {database_link}")
					conn = sqlite3.connect(database_link)
					print("Error: database link not found, could not connect to local DB !!!!!!!!!\n")
					print("Error: connect to Sample DB instead !!!!!!!!!\n")



			# Time recorded when receive data from NFC reader
			# This time will be properly formated and send to server and UI
			timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
			timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
			#print(len(timeSentToUI))

			# Read student info from database if possible
			body = read_database(conn, data, school_name_db, timeSentToUI)
			if body != None:
				send_all('NFC_card_info',body,MY_TOKEN)
				time.sleep(5.2)

			# Request data to be sent from client (our MCU) to server
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
			
			

			"""
			Standard server response format for product v.0.0.3:

			{"errorCode":"00",
			"errorMessage":"",
			"data":
				{"id":1,
				"name":"Phạm Ngọc Bảo An",
				"gender":"FEMALE",
				"studentId":"0012-22-0219",
				"firstName":"Pham Ngoc Bao ",
				"lastName":"An",
				"school":
					{"id":3,
					"name":"Tiểu học Thịnh Long A",
					"type":"SECONDARY",
					"schoolContract":
						{"id":3,
						"name":"HD0003",
						"useSelfCheckAttendance":true,
						"useNutrition":true}
					},
				"clazz":
					{"id":1,
					"name":"1A1"}
				}
			} """

			# Error code of server response	
			server_error_code = received_string["errorCode"]
			print(f"Server response error code: {server_error_code}")

			# What to do with our information? 
			# 1) Send to server and receive response data
			# OR 2) Look this information up in our local database and update database
			# OR 3) Do both of above

			# Update Time A or Time B in local database
			update_database(conn, data, timeSentToServer)

			# If our local database doesn't work, turn into server response and decode it for information
			if body == None:
				# If we're unable to decode server's response, body will be none
				# Then, mission fail. Studen information is not valid
				body = decode_server_response(server_error_code, received_string, timeSentToUI)

				# If student information is valid, send this information to UI
				if body != None:
					send_all('NFC_card_info',body,MY_TOKEN)
					# Wait for our pop-up dialog in our UI to disappear
					time.sleep(5)
				else:
					send_all('Error: Student Info Not Found',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN)
					time.sleep(5)

if __name__ == "__main__":
	main()
