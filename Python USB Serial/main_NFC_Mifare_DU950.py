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

REQAcommand = bytearray()
REQAcommand.append(0x02) # STX
REQAcommand.append(0x00) # LEN-H
REQAcommand.append(0x01) # LEN-L
REQAcommand.append(0x21) # REQA CMD
REQAcommand.append(0x20) # LRC


READKEYcommand = bytearray()
READKEYcommand.append(0x02) # STX
READKEYcommand.append(0x00) # LEN-H
READKEYcommand.append(0x0A) # LEN-L
READKEYcommand.append(0x36) # REQA CMD
READKEYcommand.append(0x00) # R mode
READKEYcommand.append(0x00) # A mode
READKEYcommand.append(0x01) # Block number of the card
for i in range(6):
	READKEYcommand.append(0xFF) #  Key[0]..[5], The key data to be stored into the secret key buffer
READKEYcommand.append(0x3d) # LRC


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
		baudrate = 115200,
		timeout = 0.5)
	
	# initialize API for connecting to server-backend
	server = 'http://171.244.207.65:7856'
	ses = Session()
	ses.headers.update({
		'Content-Type': 'application/json'})

	with open('/home/thien-nv/Downloads/API_TOKEN.txt') as f:
		MY_TOKEN = f.read()

	print (f"Token received form file: {MY_TOKEN}, type: {type({MY_TOKEN})}")


	print("Start reading !!!!!!!!!")
	send_all('Start','Start using NFC reader',MY_TOKEN) # send infomation to User interface
	# MAIN LOOP
	while (True): 
		#print(f"write to the card: {hex(int.from_bytes(READKEYcommand,byteorder='big'))}")
		ser.write(READKEYcommand) 
		#print(f"Done writing")

		in_bin = ser.read(size=32)
		#print("Read binary:")
		#print(in_bin)
		in_hex = hex(int.from_bytes(in_bin,byteorder='big'))
		#print(f"hexa read: {in_hex}")
		if in_hex[2:9] == '2001500':
			print("READ KEY command succeded")
			print(f"hexaread {in_hex}")
			#print(f"hexaread 2:9 {in_hex[2:9]}")
			print(f"hexaread 17:-2 {in_hex[17:-2]}")
			binary_str = codecs.decode(in_hex[17:-2], "hex")
			id_card = str(binary_str,'utf-8')
			print(f"ASCII code: {id_card}")


			# valid check string from usb and send to server
			if (len(id_card)>3):
				
				# sent to server 
				timeSentToServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
				timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
				#print(len(timeSentToUI))
				postData = {
						"machineId": "1234TT",
						"checkingTime": timeSentToServer,
						"cardNo": id_card,}
				res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
				print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')

				received_string = res.text
				#print(received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3])

				if (received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3]=="00"):
					
					student_info = received_string[received_string.index("data")+7:received_string.index("school")-2]
					school_info = received_string[received_string.index("school")+9:received_string.index("clazz")-3]
					class_info = received_string[received_string.index("clazz")+8:-3]

					#print(f'student_info: {student_info}\nschool_info: {school_info}\nclass_info: {class_info}\n')

					student_name = student_info[student_info.index("name")+7:student_info.index("email")-3]
					student_id = student_info[student_info.index("studentId")+12:-1]
					school_name = school_info[school_info.index("name")+7:-20]
					class_name = class_info[class_info.index("name")+7:-1]
					

					print(f'student_name_id: {student_name}, {student_id}\n'
						  f'school_name: {school_name}\nclass_name: {class_name}\n')
						  
					body = student_name + ' | ' + student_id + ' | '  + class_name + ' | ' + school_name + ' | ' + timeSentToUI + ' | ' + id_card

					send_all('NFC_card_info',body,MY_TOKEN) # send infomation to User interface
					time.sleep(3.2)


if __name__ == "__main__":
	main()
 
