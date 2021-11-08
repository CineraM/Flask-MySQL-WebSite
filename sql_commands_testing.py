# do not use this file, just for testing sql_commands

import json
import mysql.connector
import time
from datetime import datetime
import sql_commands


with open('MOCK_DATA.json') as file:
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
