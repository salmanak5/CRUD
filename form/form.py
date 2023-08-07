# import sqlite3

# # Connect to the database (if it doesn't exist, a new one will be created)
# connection = sqlite3.connect("form.db")
# cursor = connection.cursor()
# # command="CREATE TABLE IF NOT EXISTS forms(username TEXT,password TEXT,age INTEGER,phone VARCHAR,dateofbirth VARCHAR)"
# # cursor.execute(command)
# # Get user input for the number of times to run the loop
# num_inserts = int(input("Enter the number of records you want to insert: "))

# for _ in range(num_inserts):
#     # Get user input for each column data
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     age = int(input("Enter age: "))
#     phone = input("Enter phone number: ")
#     date_of_birth = input("Enter date of birth (format: DD-MM-YYYY): ")

#     # Execute the INSERT statement with column names specified and user-provided data
#     cursor.execute("INSERT INTO forms (username, password, age, phone, dateofbirth) VALUES (?, ?, ?, ?, ?)",
#                    (username, password, age, phone, date_of_birth))

# # Commit the changes to the database
# connection.commit()

# # Close the database connection
# connection.close()


import datetime
import sqlite3

def check_date_format(date_string):
    try:
        # Check if the date string can be converted to a valid date
        datetime.datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

    # Connect to the database (if it doesn't exist, a new one will be created)
connection = sqlite3.connect("form.db")
cursor = connection.cursor()

# Create the "forms" table if it doesn't exist
# cursor.execute("CREATE TABLE IF NOT EXISTS forms(username TEXT PRIMARY KEY, password TEXT, age INTEGER, phone VARCHAR, dateofbirth VARCHAR)")

# Get user input for the number of times to run the loop
num_inserts = int(input("Enter the number of records you want to insert: "))

for i in range(1,num_inserts):

    while True:
        print("enter record"+str(i))
      
        # Get user input for each column data
        username = input("Enter username: ")
        password = input("Enter password: ")
        age = int(input("Enter age: "))
        phone = input("Enter phone number: ")
        date_of_birth = input("Enter date of birth (format: DD-MM-YYYY): ")

        # Check if the username already exists in the database
        cursor.execute("SELECT COUNT(*) FROM forms WHERE username=?", (username,))
        if cursor.fetchone()[0] > 0:
            print("Username already exists. Please choose a different username.")
            continue

        # Check if the phone number already exists in the database
        cursor.execute("SELECT COUNT(*) FROM forms WHERE phone=?", (phone,))
        if cursor.fetchone()[0] > 0:
            print("Phone number already exists. Please enter a different phone number.")
            continue

        # Check if the date of birth is in the correct format
        if not check_date_format(date_of_birth):
            print("Invalid date of birth format. Please make sure you're writing it as DD-MM-YYYY.")
            continue

        # If all checks passed, break out of the loop and proceed to insert data
        break

    # Execute the INSERT statement with column names specified and user-provided data
    cursor.execute("INSERT INTO forms (username, password, age, phone, dateofbirth) VALUES (?, ?, ?, ?, ?)",
                   (username, password, age, phone, date_of_birth))

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()















