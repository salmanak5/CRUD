import sqlite3
connection=sqlite3.connect("users.db")
cursor =connection.cursor()

cursor.execute("INSERT INTO user VALUES('sajan','sajjad123','25','00000','2-12-1222')")


connection.commit()