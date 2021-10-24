'''
Testing sql commands, we are not using this file!

'''
import mysql.connector
import time
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="gym"
)

mycursor = mydb.cursor()


def create_member(id, year, month, day):
    date = datetime(year, month, day)
    formatted_date = date.strftime('%Y-%m-%d')

    sql = mycursor.execute(
        "INSERT INTO dummy (id, dob) VALUES (%s, %s)", (id, formatted_date))

    mycursor.execute(sql)
    mydb.commit()


#create_member(8, 2009, 11, 3)
sql = mycursor.execute("SELECT * FROM dummy")
data = mycursor.fetchall()
print(data)
