# do not use this file, just for testing sql_commands

import json
import mysql.connector
import time
from datetime import datetime
import sql_commands

'''
with open('members_data.json') as file:
    data = json.load(file)
    for entry in data:
        date = entry['dob'].split("/")
        date = [int(item) for item in date]
        print(date[0], date[1], date[2])
        try:
            new_user = sql_commands.create_member(entry['username'], entry['password'], entry['first_name'],
                                                  entry['last_name'], date[2], date[0], date[1], entry['height'], entry['weight'])
        except ValueError:
            pass



# sql_commands.create_class(1005,"ADVANCED Zumba","test", 25, 2021, 5, 5, 2, 30, 0)

with open('class_data.json') as file:
    data = json.load(file)
    for entry in data:
        date, t = entry['time'].split(" ")
        date = date.split("-")
        t = t.split(":")
        date = [int(item) for item in date]
        # print(date[0], date[1], date[2])
        t = [int(item) for item in t]
        # print(t[0], t[1], t[2])
        new = sql_commands.create_class(entry['classID'], entry['name'], entry['description'],
                                        entry['capacity'], date[0], date[1], date[2], t[0], t[1], t[2])
'''
# can use this to test drop class, just insert someone into registeredfor first
# sql_commands.member_drop_class("acarlisi5d",1012)

#testing trainer register for class
#sql_commands.trainer_register("DatStreetBoi",1012)
#testing the dropping of the class, this works results show in workbench
#sql_commands.trainer_drop_class("DatStreetBoi", 1012)
data = sql_commands.member_count_view()
print(data)
