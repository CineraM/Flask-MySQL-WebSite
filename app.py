from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="test"
)

cursor = mydb.cursor()


@app.route('/')
def index():
    cursor.execute("SELECT * FROM dummy")
    results = cursor.fetchall()
    return render_template('home.html', results=results)
