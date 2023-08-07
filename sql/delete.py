import sqlite3
connection=sqlite3.connect("users.db")
cursor=connection.cursor()

cursor.execute("DELETE FROM user WHERE name='akhund'")
connection.commit()