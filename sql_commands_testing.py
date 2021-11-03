# do not use this file, just for testing sql_commands

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


def query_member(q_member):
    mycursor.execute(
        f"SELECT * FROM member WHERE firstname LIKE '{q_member}%';")
    data = mycursor.fetchall()
    return data


print(query_member('Izaiah'))
