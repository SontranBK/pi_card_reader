from requests import Session
from datetime import datetime,date
import time
import json

# a list of machine id, for testing purpose
machine_Id_list =["00001",
"00002",
"00003",
"00004",
"00005",
"00006",
"00007",
"00008",
"00009",
"00010",
]

# this is our server domain
server = 'http://api.metaedu.edu.vn'

# create session
ses = Session()
ses.headers.update({
	'Content-Type': 'application/json'
})

# try each machine id in the list
for mID in machine_Id_list:
	try: 
		# try send machine id to server, which means call server
		res = ses.get(server + '/api/school-devices/getByMachineId/1234TT', json={"machineId":mID,}, auth=('user', 'user'))
		# print response to console
		print(f'\nserver response: {res.text}, type res: {type(res)}, type: {type(res.text)}\n')
	except:
		# if call server fail, then print to console
		res = "Lost connection to OCD server"
		print("Error: Lost connection to OCD server !!!!!!!!!\n")
		#send_all('Error: Lost connection to OCD server',datetime.now().strftime('%H:%M') + ', ' + date.today().strftime('%d/%m'),MY_TOKEN)
				
	time.sleep(3)

"""
Standard server response format for product v.1.0.3:

{
"errorCode":"00",
"errorMessage":"",
"data":
	{
	"name":"Meta edu",
	"logoUrl":"http://171.244.207.65:7856/api/attachments/preview?id=1",
	"backgroundUrl":"http://171.244.207.65:7856/api/attachments/preview?id=1"
	}
}
"""            
