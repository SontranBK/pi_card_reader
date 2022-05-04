#!/usr/bin/python3
 
import sys
sys.path.append('./.local/lib/python3.9/site-packages')
import time
import serial
from requests import Session
import time
from datetime import datetime,date
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging


def send_all(title,body,FCM_token):
	# [START send_all]
	# Create a list containing up to 500 messages.
	messages = [
	messaging.Message(
	    notification=messaging.Notification(title, body),
	    token=FCM_token,
	),

	#messaging.Message(
	#    notification=messaging.Notification('Price drop', '2% off all books'),
	#    topic='readers-club',
	#),

	]

	response = messaging.send_all(messages)
	# See the BatchResponse reference documentation
	# for the contents of response.
	print('{0} messages were sent successfully'.format(response.success_count))
	# [END send_all]



def main():
	# initialize firebase, API for backend-UI communication
	cred = credentials.Certificate('service-account.json')
	default_app = firebase_admin.initialize_app(cred)

	# initialize serial python, framework for reading serial USB
	ser = serial.Serial(
		port = "/dev/ttyUSB0",
		baudrate = 9600,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 2)
	
	# initialize API for connecting to server-backend
	server = 'http://171.244.207.65:7856'
	ses = Session()
	ses.headers.update({
		'Content-Type': 'application/json'})

	# define token FCM
	MY_TOKEN = 'e1k5wucJKxNJsdgl7-HQOU:APA91bFsFOfzs0X7UANy_EeH394yq71F96DYoQ88iEW9uqjOYpoEXB8UOwNzLLWms7_2PHAQzE3TyHnRE90MJkZiSZW3ZadPE8Fefftw3I-hkOC1reME5zVbr_4M9FhSApCbFZqtgvcp'

	# MAIN LOOP
	#print("Raspberry's receiving : ")

	while (True): 
		# read USB serial and convert to string   
		s = ser.readline()
		#print(f"ser.readline: {s}")
		data = s.decode("utf-8")	# decode s
		#print(f"s.decode: {data}")
		id_card = data.rstrip()	# cut "\r\n" at last of string
		print(f"id of the card: {id_card[1:11]}\n")	# print string   
		
		# valid check string from usb and send to server
		if (len(id_card)>3):
			
			# sent to server 
			timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
			timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
			#print(len(timeSentToUI))
			postData = {
					"machineId": "1234TT",
					"checkingTime": timeSentToServer,
					"cardNo": id_card[1:11],}
			res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
			#print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')

			received_string = res.text
			#print(received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3])

			if (received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3]=="00"):
				
				student_info = received_string[received_string.index("data")+7:received_string.index("school")-2]
				school_info = received_string[received_string.index("school")+9:received_string.index("clazz")-3]
				class_info = received_string[received_string.index("clazz")+8:-3]

				#print(f'student_info: {student_info}\nschool_info: {school_info}\nclass_info: {class_info}\n')

				student_name = student_info[student_info.index("name")+7:student_info.index("email")-3]
				student_id = student_info[student_info.index("studentId")+12:-1]
				school_name = school_info[school_info.index("name")+7:-1]
				class_name = class_info[class_info.index("name")+7:-1]
				

				print(f'student_name_id: {student_name}, {student_id}\n'
					  f'school_name: {school_name}\nclass_name: {class_name}\n')
					  
				body = student_name + ' | ' + student_id + ' | '  + class_name + ' | ' + school_name + ' | ' + timeSentToUI + ' | ' + id_card[1:11]

				send_all('test mess from Son',body,MY_TOKEN) # send infomation to User interface


if __name__ == "__main__":
	main()
 
