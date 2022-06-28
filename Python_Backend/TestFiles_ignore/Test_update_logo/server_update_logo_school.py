from requests import Session
from datetime import datetime,date
import time
import json

# a list of machine id, for testing purpose
mID = "00001"

# number of retry time when call server
retry_time = 0

# this is our server domain
server = 'http://api.metaedu.edu.vn'

# create session
ses = Session()
ses.headers.update({
	'Content-Type': 'application/json'
})



def have_internet():
	int_conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
	try:
		int_conn.request("HEAD", "/")
		#print("Internet: yes")
		return True
	except Exception:
		#print("Internet: no")
		return False
	finally:
        	int_conn.close()


while(retry_time < 5):
	try: 	
		if have_internet() == True:
			res = ses.get(server + '/api/school-devices/getByMachineId/1234TT', json={"machineId":mID,}, auth=('user', 'user'))
			print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')
			# check if json file "assets\ui_auto_update.json" is similar to our response
			# if similar, break			
			break

			# if not similar, modify system_setting.json file
				# if port number is 41209, set port to 41200
				# else increase port number by 1
		else:
			res = "Lost internet"
			print("Thiết bị mất kết nối internet, vui lòng kiểm tra lại kết nối internet\n"
			      "Thử kết nối lại với server sau 15 giây\n")
			time.sleep(1)
			retry_time += 1
			print(f"Retry time {retry_time}")
	except:
		res = "Lost connection to OCD server"
		print("Không thể kết nối với server, vui lòng liên hệ kĩ thuật viên\n"
			  "Thử kết nối lại với server sau 15 giây\n")
		time.sleep(1)
		retry_time += 1
		print(f"Retry time {retry_time}")



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
