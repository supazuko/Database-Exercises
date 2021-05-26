import mysql.connector
from mysql.connector import Error

def connect_movie_table():
    conn = None
    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'movie_review',
        user = 'root', password = 'sanjunipero') 
        print('Connecting to database server...')
        if conn.is_connected:
            print('Connected to database server')
            db_cursor = conn.cursor(dictionary = True)

            user_selection = int(input("""For movie table: 
            Enter 1 to insert
            Enter 2 to update
            Enter 3 to delete...
            """))

            if user_selection == 1:

                sql_insert = "INSERT INTO ratings (rating) VALUES (%s);"
                val = []
                numberOfEntries = int(input("How many records do you want to enter?: "))

                for i in range(numberOfEntries):
                    rating = input("Enter movie rating: ")
                    release_year = (input("Enter movie release year: "))
                    genre = input("Enter movie genre: ")
                    collection_in_mil = (input("Enter movie sales: "))
                    print()

                    val.append((title, release_year, genre, collection_in_mil))

                db_cursor.executemany(sql_insert, val)

                conn.commit()

                print(db_cursor.rowcount, 'record(s) was inserted')

            if user_selection == 2:
                numberOfEntries = int(input("How many fields do you want to update?: "))

                for i in range(numberOfEntries):
                    movie_id = int(input("Enter movie id: "))
                    column_name = input("Enter column name: ")
                    updated_value = input("Enter new value: ")
                    update = column_name + "=" + updated_value
                    sql_update = "UPDATE movie SET " + column_name + "=" + "\'" + updated_value + "\' WHERE movie_id = " + str(movie_id)
                    db_cursor.execute(sql_update)
                    conn.commit()
                    print(db_cursor.rowcount, 'field(s) was updated')
            
            if user_selection == 3:
                numberOfEntries = int(input("How many records do you want to delete?: ")) 
                for i in range(numberOfEntries):
                    value = input("Enter the value of the row: ")
                    column_name = input("Enter column name: ")
                    sql_delete = "DELETE from movie WHERE " + column_name + "=" + "\'" + value + "\'"
                    print()
            
                db_cursor.execute(sql_delete)

                conn.commit()

                print(db_cursor.rowcount, 'record(s) are deleted')
             
            else:
                print("Invalid selection")
                connect_movie_table()

            db_cursor.close

    except Error as e:
        print('Connection failed due to the following:', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')

connect_movie_table()