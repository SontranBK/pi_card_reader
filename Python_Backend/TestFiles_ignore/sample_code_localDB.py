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
    
# CHƯƠNG TRÌNH CHÍNH

action = 0
 
while action >= 0:
    if action == 1:
        ID = input("Nhập ID muốn thêm: ")
        STT = input("Nhập STT: ")
        CLASS = input("Nhập lớp: ")
        NAME = input("Nhập họ và tên: ")
        DOB = input("Nhập ngày tháng năm sinh (dd/mm/yyyy): ")
        GENDER = input("Nhập giới tính (MALE hoặc FEMALE): ")
        insert(STT, CLASS, NAME, ID, DOB, GENDER)
    elif action == 2:
        ID = input("Nhập ID muốn xóa: ")
        deleteStudent(ID) 
    elif action == 3:
        ID = input("Nhập ID muốn sửa: ")
        STT = input("Sửa STT thành: ")
        CLASS = input("Sửa lớp thành: ")
        NAME = input("Sửa họ và tên thành: ")
        DOB = input("Sửa ngày tháng năm sinh thành (dd/mm/yyyy): ")
        GENDER = input("Sửa giới tính thành (MALE hoặc FEMALE): ")
        update(STT, CLASS, NAME, DOB, GENDER, ID)
    elif action == 4:
        show()
    elif action == 5:
        inputID = input("Nhập ID: ")
        func(inputID)
    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm học sinh")
    print("Nhập 2: Xóa học sinh")
    print("Nhập 3: Sửa học sinh")
    print("Nhập 4: Xem danh sách học sinh hiện tại")
    print("Nhập 5: Điểm danh học sinh")
    print("Nhập 0: Thoát khỏi chương trình")
    action = int(input())
    if action == 0:
        break
