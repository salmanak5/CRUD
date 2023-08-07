import sqlite3
connection=sqlite3.connect("users.db")
cursor=connection.cursor()
# command="CREATE TABLE IF NOT EXISTS user(name TEXT,password TEXT,age INTEGER,phone VARCHAR)"
command="Alter table user add dateofbirth varchar"
cursor.execute(command)
# cursor.execute("ALTER TABLE user")
# cursor.execute("ADD DateOfBirth")
# connection.commit()
# cursor.execute("DELETE FROM user WHERE name='akhund'")
# connection.commit()