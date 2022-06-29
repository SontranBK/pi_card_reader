
import sqlite3
import time
from datetime import datetime,date
from requests import Session
import json


"""
SECTION 1: READ SYSTEM CONFIG AND DEFINE VARIABLES
"""

try: 
	with open('system_config.json') as json_file:
	    data = json.loads(json_file.read())
	    #print(data)
except:
	data = ""

# max number of retry time when call server
# retry_time is a counting variable
try:
	max_retry_time = data["server_client_config"]["maximum_retry_time"]
	print("Read system config successfully")
except:
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

ses = Session()
ses.headers.update({
    'Content-Type': 'application/json'
})


"""
SECTION 2: MAIN PROGRAM
"""

while (True):
    conn = sqlite3.connect("pi_card_reader/Database/log_retry.db")
    cursor = conn.execute(f"SELECT machineID, checkingTime, studentID, retryTimes FROM LOGTABLE")
    for row in cursor:
        if int(row[3]) < max_retry_time:
            #start = time.time()
            print(f"Found info for retry: {str(row[0])}, {str(row[1])}, {str(row[2])}")

            postData = {
                "machineId": str(row[0]),
                "checkingTime": str(row[1]),
                "studentID": str(row[2]),}
            try:
                conn.execute("DELETE FROM LOGTABLE WHERE retryTimes = 5")
                conn.commit()
            except:
                pass


            try:
                res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
                print(f'\nserver response: {res.text}, type res: {type(res)}, type: {type(res.text)}\n')
                checking_time = postData["checkingTime"]
                conn.execute("UPDATE LOGTABLE set retryTimes = 5 where checkingTime = ?",([checking_time]))
                conn.commit()
                print("Update !!!!")
            except:           
                checking_time = postData["checkingTime"]
                new_retry_time = int(row[3]) + 1
                try:
                    conn.execute("UPDATE LOGTABLE set retryTimes = ? where checkingTime = ?",(new_retry_time,checking_time))
                    print("Retry + 1 !!!!")
                except:
                    pass
            #end = time.time()
            #print("Execution time: "+str(end-start))
    time.sleep(time_break_between_retry)
