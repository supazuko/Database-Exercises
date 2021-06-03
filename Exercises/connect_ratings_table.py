import mysql.connector
from mysql.connector import Error
import stdiomask

def connect_ratings_table():
    conn = None

    host = input('Enter Host for database: ')
    database = input('Enter database name: ')
    user = input('Enter user for database: ')
    password = stdiomask.getpass("Enter password: ")

    try:
        conn = mysql.connector.connect(host=host, database=database, user=user, password=password) 
        print('Connecting to database server...')
        if conn.is_connected:
            print('Connected to database server')
            db_cursor = conn.cursor(dictionary = True)

            user_selection = int(input("""For ratings table: 
            Enter 1 to insert
            Enter 2 to update
            Enter 3 to delete...
            """))

            if user_selection == 1:

                sql_insert = "INSERT INTO ratings (rating, movie_id, reviewer_id) VALUES (%s,%s,%s);"
                val = []
                numberOfEntries = int(input("How many records do you want to enter?: "))

                for i in range(numberOfEntries):
                    rating = input("Enter movie rating: ")
                    movie_id = (input("Enter movie id: "))
                    reviewer_id = input("Enter reviewer id: ")

                    print()

                    val.append((rating, movie_id, reviewer_id))

                db_cursor.executemany(sql_insert, val)

                conn.commit()

                print(db_cursor.rowcount, 'record(s) was inserted')

            if user_selection == 2:
                numberOfEntries = int(input("How many fields do you want to update?: "))

                for i in range(numberOfEntries):
                    movie_id = (input("Enter movie id: "))
                    reviewer_id = input("Enter reviewer id: ")
                    updated_rating = input("Enter new rating: ")

                    sql_update = "UPDATE ratings SET rating = \'" + updated_rating + "\' WHERE movie_id = \'" + movie_id + "\' and reviewer_id = \'" + reviewer_id + "\'"
                    db_cursor.execute(sql_update)
                    conn.commit()
                    print(db_cursor.rowcount, 'field(s) was updated')
            
            if user_selection == 3:
                numberOfEntries = int(input("How many records do you want to delete?: ")) 
                for i in range(numberOfEntries):
                    movie_id = input("Enter movie id: ")
                    reviewer_id = input("Enter reviewer id: ")

                    sql_delete = "DELETE from ratings WHERE movie_id = \'" + movie_id + "\' and reviewer_id = \'" + reviewer_id + "\'"
                    print()
            
                db_cursor.execute(sql_delete)

                conn.commit()

                print(db_cursor.rowcount, 'record(s) are deleted')
             
            else:
                print("Invalid selection")
                connect_ratings_table()

            db_cursor.close

    except Error as e:
        print('Connection failed due to the following:', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')

connect_ratings_table()