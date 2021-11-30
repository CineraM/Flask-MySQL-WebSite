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


def create_member(username, password, firstname, lastname, year, month, day, height, weight):
    try:
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
        return True
    except:
        return False


def create_trainer(username, password, firstname, lastname, year, month, day):
    try:
        date = datetime(year, month, day)
        # date has to be passed in this format
        formatted_date = date.strftime('%Y-%m-%d')
        sql = """INSERT INTO trainer (username,
            password,
           firstname,
           lastname,
           dob
           ) VALUES(%s, %s, %s, %s, %s)"""
        val = (username, password, firstname, lastname,
               formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()  # execute and commit to the database
        return True
    except:
        return False


def create_class(classid, name, description, capacity, year, month, day, hour, min, sec):
    date = datetime(year, month, day, hour, min, sec)
    # date has to be passed in this format
    formatted_date = date.strftime('%Y-%m-%d, %H:%M:%S')
    sql = """INSERT INTO class (classID,
        name,
        description,
        capacity,
        time
        ) VALUES (%s, %s, %s, %s, %s)"""
    val = (classid, name, description, capacity, formatted_date)
    mycursor.execute(sql, val)
    mydb.commit()


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


def delete_member(user):
    sql = f"DELETE FROM member WHERE username = '{user}' "
    mycursor.execute(sql)
    mydb.commit()


def get_member(user):
    mycursor.execute(f"SELECT * FROM member WHERE username = '{user}'")
    data = mycursor.fetchall()
    return data


def delete_trainer(user):
    sql = f"DELETE FROM trainer WHERE username = '{user}' "
    mycursor.execute(sql)
    mydb.commit()


def get_trainer(user):
    mycursor.execute(f"SELECT * FROM trainer WHERE username = '{user}'")
    data = mycursor.fetchall()
    return data


def get_trainer_name(user):
    mycursor.execute(
        f"SELECT firstname FROM trainer WHERE username = '{user}'")
    data = mycursor.fetchall()
    return data[0]


def get_registered_classes(user):
    mycursor.execute(
        f"SELECT * FROM class NATURAL JOIN registeredfor WHERE username = '{user}'")
    data = mycursor.fetchall()
    return data


def get_registered_ids(user):
    mycursor.execute(
        f"SELECT classID FROM class NATURAL JOIN registeredfor WHERE username = '{user}'")
    data = mycursor.fetchall()
    return data


def get_trainer_classes(admin):
    mycursor.execute(
        f"SELECT * FROM class WHERE instructor = '{admin}'")
    data = mycursor.fetchall()
    return data
# These functions added for implementations


def member_register(username, classID):   # Returns a list with all the classes
    sql = """INSERT INTO registeredfor
    (username, classID)
    VALUES(%s, %s)"""
    sql2 = f"UPDATE class SET capacity = capacity - 1 WHERE capacity > 0 AND classID = '{classID}' "
    val = (username, classID)
    mycursor.execute(sql, val)
    mycursor.execute(sql2)
    mydb.commit()

# function that deletes a tuple from the registered for table in database


def member_drop_class(username, classID):
    sql = f"DELETE FROM registeredfor WHERE classID = '{classID}' AND username = '{username}'"
    # sql2 = f"UPDATE class SET capacity = capacity + 1 WHERE classID = '{classID}' "
    mycursor.execute(sql)
    # mycursor.execute(sql2)
    mydb.commit()

# this function updates the instructor column in the class table to the username of a trainer


def trainer_register(username, classID):
    sql = f"UPDATE class SET instructor = '{username}' WHERE classID = '{classID}'"
    mycursor.execute(sql)
    mydb.commit()

# this is a function that sets the instructor to NULL for a class in the class table when a trainer chooses to not teach the class


def trainer_drop_class(username, classID):
    sql = f"UPDATE class SET instructor = NULL WHERE classID = '{classID}' and instructor = '{username}'"
    mycursor.execute(sql)
    mydb.commit()

# this is the view for a trainer to see the number of members inthe class they are teaching
def member_count_view():
    sql = "SELECT covidawarenessview.name, covidawarenessview.NumberOfMembers,covidawarenessview.time FROM gym.covidawarenessview;"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data
