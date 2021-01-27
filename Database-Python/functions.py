import mysql.connector, os
from os import environ
from mysql.connector import connect
import connection as c


def readStudentInfo():  
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM student')
        for row in cursor:
            print(f'''
            id................ {row[0]}
            First Name........ {row[1]}
            Last Name......... {row[2]}
            Age............... {row[3]}
            ''')
        cursor.close() 
        conn.close() 
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)


# function to insert info into student table
def insertStudentInfo(fname, lname, age, phone):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO student (fname, lname, age, phone) VALUES ('{fname}', '{lname}', {age}, '{phone}')")
        conn.commit()
        readStudentInfo()
        cursor.close() 
        conn.close() 
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
    

# ******** For Windows **********
# First install python-dotenv

# from dotenv import load_dotenv
# import os
# from os import getenv
# load_dotenv()

# create .env file under the root directory/folder and add the environment variable

# conn = connect(
#     host=getenv('DB_NAME'),
#     user=getenv('DB_USER'),
#     password=getenv('DB_URL'),
#     database=getenv('DB_PASSWORD')
#     port=getenv('DB_PORT')
# )
# ****** End of Windows ********* 

# ******** macOS ************
# conn = connect(
#     host= environ.get('DB_URL'),
#     user=environ.get('DB_USER'),
#     password=environ.get('DB_PASSWORD'),
#     database=environ.get('DB_NAME')
# )
# ******* End of macOS ************