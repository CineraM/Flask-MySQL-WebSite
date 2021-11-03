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


def get_members():           # Returns a list with all the members, flask formats it into the html
    mycursor.execute('SELECT * FROM member;')
    data = mycursor.fetchall()
    return data


def query_member(q_member):  # Query used in the serch bar of the members page
    mycursor.execute(
        f"SELECT * FROM member WHERE firstname LIKE '{q_member}%';")
    data = mycursor.fetchall()
    return data


def get_trainers():         # Returns a list with all the trainers
    mycursor.execute('SELECT * FROM trainer;')
    data = mycursor.fetchall()
    return data


def query_trainer(q_trainer):  # Query used in the serch bar of the trainers page
    mycursor.execute(
        f"SELECT * FROM trainer WHERE firstname LIKE '{q_trainer}%';")
    data = mycursor.fetchall()
    return data


def get_classes():          # Returns a list with all the classes
    mycursor.execute('SELECT * FROM class;')
    data = mycursor.fetchall()
    return data


def query_class(q_class):  # Query used in the serch bar of the classes page
    mycursor.execute(
        f"SELECT * FROM class WHERE name LIKE '{q_class}%';")
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
