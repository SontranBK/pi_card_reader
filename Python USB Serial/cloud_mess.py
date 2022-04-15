from __future__ import print_function

from datetime import datetime,date

import time

import firebase_admin

from firebase_admin import credentials

from firebase_admin import messaging


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
    cred = credentials.Certificate('service-account.json')
    default_app = firebase_admin.initialize_app(cred)
    

    with open('C:/Users/ThienNV/Downloads/API_TOKEN.txt') as f:
        MY_TOKEN = f.read()

    student_name = 'Tran Van A'
    student_id = '0001_22_672'
    class_name = '7A1'
    school_name = "High School"
    timeSentToUI = datetime.now().strftime('%H:%M:%S') + ', ' + date.today().strftime('%d/%m/%Y')
    id_card = "0012071984"

    
    body = student_name + ' | ' + student_id + ' | '  + class_name + ' | ' + school_name + ' | ' + timeSentToUI + ' | ' + id_card
    while (True):       
        send_all('NFC_card_info',body,MY_TOKEN) # send infomation to User interface
        time.sleep(10)

if __name__ == "__main__":
    main()
