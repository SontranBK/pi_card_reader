from requests import Session
from datetime import datetime,date
import time
import json
"""
# New student ID
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


server = 'http://171.244.207.65:7856'


ses = Session()
ses.headers.update({
	'Content-Type': 'application/json'
})

for student_id in ID_list:
	time_sent_toServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
	#print(f"\n\n\ntime sent to server: {time_sent_toServer}")
	# 0012071984
	# 0013719878
	postData = {
	        "machineId": "00001",
	        "checkingTime": time_sent_toServer,
	        "studentID": str(student_id),
	        # if we use new student ID, don't need to convert to str
	}
	try: 
		res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
		print(f'\nserver response: {res.text}, type res: {type(res)}, type: {type(res.text)}\n')

		received_string = json.loads(res.text)
		print(received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3])
	except:
		print("Error: Lost connection to OCD server !!!!!!!!!\n")
		received_string = {"errorCode":"","errorMessage":""}


	server_error_code = received_string["errorCode"]

	if server_error_code == '00':
		student_name = received_string["data"]["name"]
		student_id = received_string["data"]["studentId"]
		school_name = received_string["data"]["school"]["name"]
		class_name = received_string["data"]["clazz"]["name"]

		print(f'\n\nstudent_name_id: {student_name}, {student_id}\n'
		f'school_name: {school_name}\nclass_name: {class_name}\n')

	else:
		print("Server response Error code # 00!!!!!!!")
	




	time.sleep(3)
                

