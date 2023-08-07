
import sqlite3
import datetime

def check_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string,'%d-%m-%Y')
        return True
    except ValueError:
        return False


connnection=sqlite3.connect("newform.db")
cursor=connnection.cursor()

# command="CREATE TABLE IF NOT EXISTS newform(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,f_name TEXT,password TEXT,phone VARCHAR,date_of_birth VARCHAR)"
# command="Alter table newform add phone VARCHAR"
# cursor.execute(command)

# connnection.commit()
# cursor.execute(command)
num_insert=int(input("ENTER THE NUMBER OF RECORDS YOU WANT TO INSERT"))
for i in range(num_insert):
    
    while True:
        print("enter record",str(i))
        
        # id=input("enter the id no: ")
        username=input("ENTER THE USERNAME: ")
        f_name=input("ENTER FATHER NAME: ")
        password=input("ENTER YOUR PASSWORD: ")
        phone=input("ENTER YOUR PHONE NUMBER")
        date_of_birth=input("ENTER YOUR DATE OF BIRTH  (FORMAT DD-MM-YYYY): ")
        
        
        cursor.execute("SELECT COUNT(*) FROM newform WHERE username=?",(username,))
        if cursor.fetchone()[0]>0:
            print("USERNAME ALREADY EXISTS. PLEASE CHOOSE DIFFERENT USERNAME")
            continue
        
        
        if not check_date_format(date_of_birth):
            print("INVALID DATE OF BIRTH FORMAT PLEASE MAKE SURE YOU ARE WRITING AS DD-MM-YYYY.:")
            continue
        
        cursor.execute(f"SELECT COUNT(*) FROM newform WHERE phone=? ",(phone,))
        if cursor.fetchone()[0] > 0:
            print("PHONE NUMBER IS ALREADY EXIST. PLEASE CHOOSE DIFFERENT PHONE NUMBER ")
            continue
        
        break
    cursor.execute("INSERT INTO newform (username, f_name,password, phone,date_of_birth) VALUES(?,?,?,?,?)",
                   (username, f_name, password,phone,date_of_birth))
connnection.commit()
connnection.close()