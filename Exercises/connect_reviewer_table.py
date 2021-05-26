import mysql.connector
from mysql.connector import Error

def connect_reviewer_table():
    conn = None
    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'movie_review',
        user = 'root', password = 'sanjunipero') 
        print('Connecting to database server...')
        if conn.is_connected:
            print('Connected to database server')
            db_cursor = conn.cursor(dictionary = True)

            user_selection = int(input("""For reviewers table: 
            Enter 1 to insert
            Enter 2 to update
            Enter 3 to delete...
            """))

            if user_selection == 1:
                sql_insert= "INSERT INTO reviewers (first_name, last_name) VALUES (%s, %s);"

                val = []
                numberOfEntries = int(input("How many records do you want to enter?: "))

                for i in range(numberOfEntries):
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    
                    print()

                    val.append((first_name, last_name))
                db_cursor.executemany(sql_insert, val)

                conn.commit()

                print(db_cursor.rowcount, 'record(s) are inserted')

            if user_selection == 2:
                numberOfEntries = int(input("How many fields do you want to update?: "))

                for i in range(numberOfEntries):
                    column_name = input("Enter column name: ")
                    updated_value = input("Enter new value: ")
                    reviewer_id = int(input("Enter reviewer id: "))
                    update = column_name + "=" + updated_value
                    # val.append((first_name, last_name))
                    sql_update = "UPDATE reviewers SET " + column_name + "=" + "\'" + updated_value + "\' WHERE reviewer_id = " + str(reviewer_id)
                    # values = (first_name, reviewer_id)
                    db_cursor.execute(sql_update)
                    conn.commit()
                    print(db_cursor.rowcount, 'field(s) are updated')

            if user_selection == 3:
                numberOfEntries = int(input("How many records do you want to delete?: ")) 
                for i in range(numberOfEntries):
                    value = input("Enter the value of the row: ")
                    column_name = input("Enter column name: ")
                    # reviewer_id = int(input("Enter reviewer id: "))
                    
                    sql_delete = "DELETE from reviewers WHERE " + column_name + "=" + "\'" + value + "\'"
                    print()

                    # val.append((first_name, last_name))
            
                db_cursor.execute(sql_delete)

                conn.commit()

                print(db_cursor.rowcount, 'record(s) are deleted')
             
            else:
                print("Invalid selection")
                connect_reviewer_table()

            db_cursor.close

    except Error as e:
        print('Connection failed due to the following:', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')

connect_reviewer_table()