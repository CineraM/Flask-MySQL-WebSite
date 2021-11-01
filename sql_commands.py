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


def get_members():  # Returns a list, flask formats it into the html
    mycursor.execute('SELECT * FROM member;')
    data = mycursor.fetchall()
    return data


def get_trainers():
    mycursor.execute('SELECT * FROM trainer;')
    data = mycursor.fetchall()
    return data


def create_member(username, password, firstname, lastname, year, month, day, height, weight):
    date = datetime(year, month, day)
    # date has to be passed in this format
    formatted_date = date.strftime('%Y-%m-%d')
    sql = """INSERT INTO member (username,
        password,
       firstname,
       lastname,
       dob,
       height,
       weight
       ) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    val = (username, password, firstname, lastname,
           formatted_date, height, weight)
    mycursor.execute(sql, val)
    mydb.commit()  # execute and commit to the database
# we will probably need to add a try and catch for input validation


def delete_member(user):
    sql = f"DELETE FROM member WHERE username = '{user}' "
    mycursor.execute(sql)
    mydb.commit()
