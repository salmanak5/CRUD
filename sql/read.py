import sqlite3
connection=sqlite3.connect("users.db")
cursor=connection.cursor()

cursor.execute("SELECT * FROM user")
result=cursor.fetchall()
print(result)

