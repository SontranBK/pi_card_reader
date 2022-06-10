import sqlite3
import xlrd
# Give the location of the file
loc = ("lehoan.xls")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#connect to database
conn = sqlite3.connect('LH_local_db.db')

list_class = ("4/1","4/2","4/3","4/4","4/5","4/6","4/7","4/8")
flag = 0
#INSERT DATA INTO DATABASE
for i in range(sheet.nrows):
    if sheet.cell_value(i,3) == list_class[0]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_1 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);
    elif sheet.cell_value(i,3) == list_class[1]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_2 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    elif sheet.cell_value(i,3) == list_class[2]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_3 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    elif sheet.cell_value(i,3) == list_class[3]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_4 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    elif sheet.cell_value(i,3) == list_class[4]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_5 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    elif sheet.cell_value(i,3) == list_class[5]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_6 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    elif sheet.cell_value(i,3) == list_class[6]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_7 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    elif sheet.cell_value(i,3) == list_class[7]:
        records = sheet.row_values(i)
        stmt = "INSERT INTO class4_8 (STT,NAME,ID,CLASS_x,SEX)";
        stmt += "values (?,?,?,?,?);"
        in_put = (records[0],records[1],records[2],records[3],records[4])
        conn.execute(stmt,in_put);   
    else:
        print("hoc sinh "+ str(sheet.row_values(i))+" bi loi lop")   
        flag = 1

if flag == 0:
    conn.commit()
    print ("Records created successfully");
    conn.close()