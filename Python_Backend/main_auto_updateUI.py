from requests import Session
from datetime import datetime,date
import time
import json
try:
    import httplib  # python < 3.0
except:
    import http.client as httplib


"""
SECTION 1: READ SYSTEM CONFIG AND DEFINE VARIABLES
"""

min_web_port = 41200
max_web_port = 41205

# parse json config file
try: 
	with open('system_config.json') as json_file:
	    data = json.loads(json_file.read())
	    #print(data)
except:
	data = ""

# read machine id from json
try: 
	mID = data["machine_id"]
	print("Read system config successfully")
except:
	mID = "00001"
	print("FAIL to read system config")

# max number of retry time when call server
# retry_time is a counting variable
try:
	retry_time = 0
	max_retry_time = data["server_client_config"]["maximum_retry_time"]
	print("Read system config successfully")
except:
	retry_time = 0
	max_retry_time = 5
	print("FAIL to read system config")

# this is our server domain
try:
	server = data["server_client_config"]["server_domain"]
	print("Read system config successfully")
except:
	server = 'http://api.metaedu.edu.vn'
	print("FAIL to read system config")

# time between two retry time, if failed
try:
	time_break_between_retry = data["server_client_config"]["time_break_between_retry"]
	print("Read system config successfully")
except:
	time_break_between_retry = 30
	print("FAIL to read system config")

# check web port and set to valid port if error
try:
	if not(min_web_port <= data["web_port"] <= max_web_port):
		data["web_port"] = min_web_port
		jsonFile = open("system_config.json", "w+")
		jsonFile.write(json.dumps(data))
		jsonFile.close()
	print("Check web port successfully")
except:
	print("FAIL to check web port")


"""
SECTION 2: FUNCTION DEFINATION
"""

# create session
ses = Session()
ses.headers.update({
	'Content-Type': 'application/json'
})

# check internet function
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

# check whether json response is similar to json saved in device
def check_json_equal(res):
	try: 
		json_saved_data = json.load(open('pi_card_reader/assets/ui_auto_update.json'))
		server_res_json = json.loads(res.text)
		print(f"Hai file json:\n{json_saved_data}\n{server_res_json}\n")
		if json_saved_data == server_res_json:
			return True
		else:
			return False
	except:
		return True

"""
SECTION 3: MAIN PROGRAM
"""

# call server for UI update info
while(retry_time < max_retry_time):

	if have_internet() == True:
		try:
			res = ses.get(server + '/api/school-devices/getByMachineId/' + mID, json={"machineId":mID,}, auth=('user', 'user'))
			print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')
		except: 
			res = "Lost connection to OCD server"
			print("\nKhông thể kết nối với server, vui lòng liên hệ kĩ thuật viên\n"
				  "Thử kết nối lại với server sau 30 giây\n")
			time.sleep(time_break_between_retry)
			retry_time += 1
			print(f"\nThử kết nối lại với server lần thứ {retry_time}\n")
			continue
		# check if json file "assets\ui_auto_update.json" is similar to our response
		# if similar, break	=> keep port, do not re-build
		if check_json_equal(res) == True:
			print("Giữ nguyên giao diện, không update")
			jsonFile = open("system_config.json", "r") # Open the JSON file for reading
			data = json.load(jsonFile) # Read the JSON into the buffer
			jsonFile.close() # Close the JSON file

			# MODIFY REQUIRE REBUILD 
			data["required_rebuild"] = 0
			jsonFile = open("system_config.json", "w+")
			jsonFile.write(json.dumps(data))
			jsonFile.close()
			break
		# if not similar, modify system_config.json file
		else:
			try:
				print("Server yêu cầu update giao diện")
				with open("pi_card_reader/assets/ui_auto_update.json", "w+") as ui_auto_update_file:
					ui_auto_update_file.write(res.text)
				jsonFile = open("system_config.json", "r") # Open the JSON file for reading
				data = json.load(jsonFile) # Read the JSON into the buffer
				jsonFile.close() # Close the JSON file

				# MODIFY REQUIRE REBUILD 
				data["required_rebuild"] = 1
				# MODIFY WEB PORT
				# if port number is 41205, set port to 41200
				if data["web_port"] == max_web_port:
					data["web_port"] = min_web_port
					jsonFile = open("system_config.json", "w+")
					jsonFile.write(json.dumps(data))
					jsonFile.close()
				# else increase port number by 1
				else:
					data["web_port"] += 1
					jsonFile = open("system_config.json", "w+")
					jsonFile.write(json.dumps(data))
					jsonFile.close()
				break
			except:
				print("\nFAIL to modify web port\n")
				break

	else:
		res = "Lost internet"
		print("\nThiết bị mất kết nối internet, vui lòng kiểm tra lại kết nối internet\n"
		      "Thử kết nối lại với server sau 30 giây\n")
		time.sleep(time_break_between_retry)
		retry_time += 1
		print(f"\nThử kết nối lại với server lần thứ {retry_time}\n")

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
