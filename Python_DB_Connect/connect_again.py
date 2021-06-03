import mysql.connector
from mysql.connector import Error
import stdiomask

def connect_again_fetch():
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

            sql_select_query = "select * from human"
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print('Total number of rows in human is: ', cursor.rowcount)

            print('\nPrinting each buyer record')
            for row in records:
                for i in row:
                    print(i, ": ", row[i])
                print() 
                # print("ID: ", row[0])
                # print("Name: ", row[1])
                # print("Color: ", row[2])
                # print("Gender: ", row[2])
                # print("Blood group: ", row[4], '\n')

    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown')

connect_again_fetch()