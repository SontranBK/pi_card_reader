
from datetime import datetime,date

import time

import firebase_admin

from firebase_admin import credentials

from firebase_admin import messaging


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
		#print('{0} messages were sent successfully'.format(response.success_count))
		print(f'{response.success_count} messages were sent successfully')
		if (response.success_count == 0):
			print("Fail to connect to UI")
			os.system('reboot')	
		# [END send_all]
	except:
		pass
		print("Error: Unable to connect with UI !!!!!!!!!\n")

def main():
    cred = credentials.Certificate('service-account.json')
    default_app = firebase_admin.initialize_app(cred)
    

	# Initialize firebase TOKEN API
	try: 
		with open('/home/metaedu/Downloads/API_TOKEN.txt') as f:
			MY_TOKEN = f.read()
		print (f"Token received form file: {MY_TOKEN}, type: {type({MY_TOKEN})}")
	except:
		print("Error: UI Token not found !!!!!!!!!\n")
		MY_TOKEN = 'c7y9di1Dwje8TXegJiyBZX:APA91bH-SZpjbjx2YWl0MSMb4FIkSIvzbncn7PQjHUvcqaKdNPFrv9YdcJvEffdB4DUDe5l4ip1DO88o4Du9xinaWTubXWUXGsW-G8Qn36S6WJJ5LJ8i64Wdj-CxVuEFHdNWfo8t_Oj1'
    
    while (True):       
        send_all('Error: Wrong data format',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN)
        time.sleep(10)
        send_all('Error: Hexa not valid',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN)
        time.sleep(10)
        send_all('Error: Lost connection to OCD server',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN)
        time.sleep(10)
        send_all('Error: Student Info Not Found',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN)
        time.sleep(10)
		send_all('Error: Reader not connected',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN) # send infomation to User interface
        time.sleep(10)

if __name__ == "__main__":
    main()
