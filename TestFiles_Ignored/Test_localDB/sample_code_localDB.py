import sqlite3
import time
from datetime import datetime,date

def show():
    conn = sqlite3.connect("D:\\Desktop\\prj7\\29_06_22.db")
    cur = conn.cursor()
        
    cur.execute(f"SELECT * FROM STUDENTS")
    for row in cur:
        print(row)
    conn.close()

def insert(STT=" ", CLASS=" ", NAME=" ", ID=" ", DOB=" ", GENDER=" ") :
    conn = sqlite3.connect("D:\\Desktop\\prj7\\29_06_22.db")
    cur = conn.cursor()
    
    cur.execute(f"INSERT INTO STUDENTS (STT, CLASS, NAME, ID, DOB, GENDER) VALUES (?,?,?,?,?,?)",
                (STT, CLASS, NAME, ID, DOB, GENDER))
    conn.commit()
    conn.close()

def deleteStudent(ID):
    conn = sqlite3.connect("D:\\Desktop\\prj7\\29_06_22.db")
    cur = conn.cursor()
        
    cur.execute(f"DELETE FROM STUDENTS WHERE ID = ?", (ID,))
    conn.commit()
    conn.close()
        
def update(STT=" ", CLASS=" ", NAME=" ", DOB=" ", GENDER=" ", ID = " ") :
    conn = sqlite3.connect("D:\\Desktop\\prj7\\29_06_22.db")
    cur = conn.cursor()
        
    cur.execute(f"UPDATE STUDENTS SET STT = ?, CLASS = ?, NAME = ?, DOB = ?, GENDER = ? WHERE ID = ?",
                (STT, CLASS, NAME, DOB, GENDER, ID))
    conn.commit()
    conn.close()

def func(inputID) :
    conn = sqlite3.connect("D:\\Desktop\\prj7\\29_06_22.db")
    print ("Opened database successfully\n")
    
    timeSentToServer = date.today().strftime('%Y-%m-%d')
    print(f"time sent to server: {timeSentToServer}")
    start = time.time()
    
    cursor = conn.execute(f"SELECT name, id, DOB, time_a, error_code_a, time_b, error_code_b from STUDENTS where ID = {inputID}")
    for row_tuple in cursor:
        row = list(row_tuple)
        print (f"\nFind student with following info:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
        if (row[3] == None):
            row[3] = timeSentToServer
            conn.execute(f"UPDATE STUDENTS set TIME_A = {timeSentToServer} where ID = {inputID}")
            conn.commit()
            print (f"After updating time:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
        else:
            row[5] = timeSentToServer
            conn.execute(f"UPDATE STUDENTS set TIME_B = {timeSentToServer} where ID = {inputID}")
            conn.commit()
            print (f"After updating time:\nNAME = {row[0]}\nID = {row[1]}\nDoB = {row[2]}\nTime A = {row[3]}\nTime B = {row[5]}\n")
            row_tuple = tuple(row)
    end = time.time()
    print("Execution time: "+str(end-start))
	
    conn.close()
    
# CH????NG TR??NH CH??NH

action = 0
 
while action >= 0:
    if action == 1:
        ID = input("Nh???p ID mu???n th??m: ")
        STT = input("Nh???p STT: ")
        CLASS = input("Nh???p l???p: ")
        NAME = input("Nh???p h??? v?? t??n: ")
        DOB = input("Nh???p ng??y th??ng n??m sinh (dd/mm/yyyy): ")
        GENDER = input("Nh???p gi???i t??nh (MALE ho???c FEMALE): ")
        insert(STT, CLASS, NAME, ID, DOB, GENDER)
    elif action == 2:
        ID = input("Nh???p ID mu???n x??a: ")
        deleteStudent(ID) 
    elif action == 3:
        ID = input("Nh???p ID mu???n s???a: ")
        STT = input("S???a STT th??nh: ")
        CLASS = input("S???a l???p th??nh: ")
        NAME = input("S???a h??? v?? t??n th??nh: ")
        DOB = input("S???a ng??y th??ng n??m sinh th??nh (dd/mm/yyyy): ")
        GENDER = input("S???a gi???i t??nh th??nh (MALE ho???c FEMALE): ")
        update(STT, CLASS, NAME, DOB, GENDER, ID)
    elif action == 4:
        show()
    elif action == 5:
        inputID = input("Nh???p ID: ")
        func(inputID)
    print("Ch???n ch???c n??ng mu???n th???c hi???n:")
    print("Nh???p 1: Th??m h???c sinh")
    print("Nh???p 2: X??a h???c sinh")
    print("Nh???p 3: S???a h???c sinh")
    print("Nh???p 4: Xem danh s??ch h???c sinh hi???n t???i")
    print("Nh???p 5: ??i???m danh h???c sinh")
    print("Nh???p 0: Tho??t kh???i ch????ng tr??nh")
    action = int(input())
    if action == 0:
        break
