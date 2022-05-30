
import sqlite3
import time
from datetime import datetime,date
from requests import Session
import json



server = 'http://171.244.207.65:7856'


ses = Session()
ses.headers.update({
    'Content-Type': 'application/json'
})

while (True):
    conn = sqlite3.connect("pi_card_reader/Database/log_retry.db")
    cursor = conn.execute(f"SELECT machineID, checkingTime, studentID, retryTimes FROM LOGTABLE")
    for row in cursor:
        if int(row[3]) < 5:
            start = time.time()
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
            end = time.time()
            print("Execution time: "+str(end-start))
    time.sleep(30)
