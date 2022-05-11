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

def read_NFC_card(ser):
	ser.write(READKEY4command) 
	in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
	if in_hex[2:9] == '2001500':
		data = str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')		
		ser.write(READKEY5command)
		in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
		if in_hex[2:9] == '2001500':
			data = data + str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')			
			ser.write(READKEY6command)		
			in_hex = hex(int.from_bytes(ser.read(size=32),byteorder='big'))
			if in_hex[2:9] == '2001500':
				data = data + str(codecs.decode(in_hex[17:-2], "hex"),'utf-8')	
				#print(f"data: {data}")
			try:
				class_name = data[:data.index("|")]
				rest = data[data.index("|")+1:]
				student_id = rest[:rest.index("|")]
				#print(f"class name: {class_name}; student ID: {student_id}")
				return class_name, student_id
			except:
				pass
				

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



def main():
	# initialize firebase, API for backend-UI communication
	cred = credentials.Certificate('service-account.json')
	default_app = firebase_admin.initialize_app(cred)

	# initialize API for connecting to server-backend
	
	server = 'http://171.244.207.65:7856'
	ses = Session()
	ses.headers.update({
		'Content-Type': 'application/json'})
	
	try: 
		with open('/home/thien-nv/Downloads/API_TOKEN.txt') as f:
			MY_TOKEN = f.read()
		print (f"Token received form file: {MY_TOKEN}, type: {type({MY_TOKEN})}")
	except:
		print("Error: UI Token not found !!!!!!!!!\n")
		MY_TOKEN = 'c7y9di1Dwje8TXegJiyBZX:APA91bH-SZpjbjx2YWl0MSMb4FIkSIvzbncn7PQjHUvcqaKdNPFrv9YdcJvEffdB4DUDe5l4ip1DO88o4Du9xinaWTubXWUXGsW-G8Qn36S6WJJ5LJ8i64Wdj-CxVuEFHdNWfo8t_Oj1'
		

	# initialize serial python, framework for reading serial USB
	#try:
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 115200,
		timeout = 0.05)
	print("Start reading !!!!!!!!!\n")
	send_all('Start: Start using NFC reader',datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y'),MY_TOKEN) # send infomation to User interface
	
	# MAIN LOOP
	while (True): 
		data = read_NFC_card(ser)
		#print(f"Received data: {data}")

		# valid check string from usb and send to server
		if data != None:
			
			# sent to server 
			timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
			timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
			#print(len(timeSentToUI))
			postData = {
					"machineId": "00001",
					"checkingTime": timeSentToServer,
					"cardNo": data[1],}
			try: 
				res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
				print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')

				received_string = res.text
				#print(received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3])
			except:
				print("Error: Lost connection to OCD server !!!!!!!!!\n")
				send_all('Error: Lost connection to OCD server',MY_TOKEN) # send infomation to User interface
				received_string = 'errorCode,errorMessage'
			server_error_code = received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3]	
			
			if (server_error_code=="00"):
				
				student_info = received_string[received_string.index("data")+7:received_string.index("school")-2]
				school_info = received_string[received_string.index("school")+9:received_string.index("clazz")-3]
				class_info = received_string[received_string.index("clazz")+8:-3]

				print(f'student_info: {student_info}\nschool_info: {school_info}\nclass_info: {class_info}\n')

				student_name = student_info[student_info.index("name")+7:student_info.index("gender")-3]
				student_id = student_info[student_info.index("studentId")+12:student_info.index("firstName")-3]
				school_name = school_info[school_info.index("name")+7:school_info.index("type")-3]
				class_name = class_info[class_info.index("name")+7:-1]
				

				print(f'student_name_id: {student_name}, {student_id}\n'
					  f'school_name: {school_name}\nclass_name: {class_name}\n')
					  
				body = student_name + ' | ' + student_id + ' | '  + class_name + ' | ' + school_name + ' | ' + timeSentToUI + ' | ' + id_card
			
			
			conn = sqlite3.connect('/home/thien-nv/pi_card_reader/Database/SampleDB.db')
			cursor = conn.execute(f"SELECT name, id, dateofbirth, time_a, error_code_a, time_b, error_code_b from CLASS_{data[0]} where ID = {data[1]}")
			for row in cursor:
				print (f"\nFind student with following info:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
				print (f"Current updating time:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
				
				if (row[3] == None):
					conn.execute("UPDATE CLASS_{} set TIME_A = ? where ID = ?".format(data[0]),(timeSentToServer,data[1]))
					conn.commit()
				else:
					conn.execute("UPDATE CLASS_{} set TIME_B = ? where ID = ?".format(data[0]),(timeSentToServer,data[1]))
					conn.commit()
					
			body = row[0] + ' | ' + data[1] + ' | '  + data[0] + ' | ' + 'Tieu hoc Thinh Long' + ' | ' + timeSentToUI + ' | ' + '000000000'
				
			send_all('NFC_card_info',body,MY_TOKEN) # send infomation to User interface
			time.sleep(5.2)
				
if __name__ == "__main__":
	main()
