from requests import Session
from datetime import datetime,date
import time
import json

# a list of machine id, for testing purpose
mID = "00001"

# this is our server domain
server = 'http://api.metaedu.edu.vn'

# create session
ses = Session()
ses.headers.update({
	'Content-Type': 'application/json'
})

while(res != "Lost internet" and res != "Lost connection to OCD server" and retry_time > 5)
	try: 	
		if have_internet() == True:
			res = ses.get(server + '/api/school-devices/getByMachineId/1234TT', json={"machineId":mID,}, auth=('user', 'user'))
			print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')
		else:
			res = "Lost internet"
			print("Error: "+res+" !!!!!!!!!\n")
	except:
		res = "Lost connection to OCD server"
		print("Error: "+res+" !!!!!!!!!\n")	
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
