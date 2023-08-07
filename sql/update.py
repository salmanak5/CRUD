import sqlite3
connection=sqlite3.connect("users.db")
cursor=connection.cursor()

cursor.execute("UPDATE user SET dateofbirth='20-1-2023' ")
connection.commit()