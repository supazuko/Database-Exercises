import mysql.connector
from mysql.connector import Error

def connect_insert():
    conn = None
    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'demo',
        user = 'root', password = 'sanjunipero') 
        print('Connecting to database server...')
        if conn.is_connected:
            print('Connected to database server')
            db_cursor = conn.cursor()

            # Create a variable to contain the sql query to be executed
            sql = "insert into Human(humanId, name, color, gender, bloodgroup) Values (%s, %s, %s, %s, %s)"

            # Create a list variable to conatain all the values we want to insert into the human table
            val = []

            entryNumber = int(input("How many records do you want to enter?: "))

            for i in range(entryNumber):
                humanId = input("Enter your ID: ")
                name = input("Enter your name: ")
                color = input("Enter your color: ")
                gender = input("Enter your gender: ")
                bloodGroup = input("Enter your blood group: ")
                print()

                val.append((humanId, name, color, gender, bloodGroup))


            # val = [
            #     ('1013', 'Hannah', 'White', 'Female', 'B-'),
            #     ('1014', 'Michael', 'Brown', 'Male', 'O-'),
            #     ('1015', 'sandy', 'Black', 'Female', 'B+'),
            # ]
            # Execute the query using the execute many function
            db_cursor.executemany(sql, val)

            # Commit to the database
            conn.commit()

            # Print a success message
            print(db_cursor.rowcount, 'rows are inserted')

            # Close the cursor
            db_cursor.close

    except Error as e:
        print('Connection failed due to the following', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')

connect_insert()