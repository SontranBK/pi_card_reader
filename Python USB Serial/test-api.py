from requests import Session
from datetime import datetime,date
import time

server = 'http://171.244.207.65:7856'


ses = Session()
ses.headers.update({
	'Content-Type': 'application/json'
})

while (True):
    time_sent_toServer = date.today().strftime('%Y-%m-%d') + ' ' + datetime.now().strftime('%H:%M:%S')
    #print(time_sent_toServer)
    # 0012071984
    # 0013719878
    postData = {
            "machineId": "1234TT",
            "checkingTime": time_sent_toServer,
            "cardNo": "0012071984",
    }
    res = ses.post(server + '/api/self-attendances/checking', json=postData, auth=('user', 'user'))
    print(f'{res.text}, type res: {type(res)}, type: {type(res.text)}\n')

    received_string = res.text
    #print(received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3])

    if (received_string[received_string.index("errorCode")+12:received_string.index("errorMessage")-3]=="00"):
        
        student_info = received_string[received_string.index("data")+7:received_string.index("school")-2]
        school_info = received_string[received_string.index("school")+9:received_string.index("clazz")-3]
        class_info = received_string[received_string.index("clazz")+8:-3]

        print(f'student_info: {student_info}\nschool_info: {school_info}\nclass_info: {class_info}\n')

        student_name = student_info[student_info.index("name")+7:student_info.index("email")-3]
        student_id = student_info[student_info.index("studentId")+12:-1]
        school_name = school_info[school_info.index("name")+7:-1]
        class_name = class_info[class_info.index("name")+7:-1]

        print(f'student_name_id: {student_name}, {student_id}\n'
              f'school_name: {school_name}\nclass_name: {class_name}\n')
    time.sleep(5)
                

