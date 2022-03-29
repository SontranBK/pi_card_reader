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
    
    MY_TOKEN = 'c4lKtm9mNAS-mWecWYGAp8:APA91bEAH3leGVYpByPi9wC5-cBeI_k-EmT6P3ZkPKiDBIwVlyNG0BmX3VdxMLdzUillcqNs9prTGIHYjgQeIyBOp-yfergkSy7K80Yyri_m4PaohTL_LugJIOKUG3GNtRmbIQ2DRcZp'

    name = 'Tran Van A'
    student_class = '71A'
    student_id = '0013719878'
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = date.today().strftime('%d/%m/%Y')

    
    body = name + ' | ' + student_class + ' | ' + student_id + ' | ' + current_time + ', ' + current_date
    while (True):       
        send_all('test mess from Son',body,MY_TOKEN)
        time.sleep(10)

if __name__ == "__main__":
    main()
