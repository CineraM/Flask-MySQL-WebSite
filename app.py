from flask import Flask, render_template, url_for, request, redirect
import sql_commands

from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')     # home root
def home_page():
    return render_template('home.html')


@app.route('/member', methods=['GET', 'POST'])  # display all members root
def members():
    q = request.args.get('q')                   # search bar implementation
    if q:
        members = sql_commands.query_member(q)
    else:
        members = sql_commands.get_members()
    return render_template('member.html', results=members)


@app.route('/trainer', methods=['GET', 'POST'])  # display all trainers root
def trainers():
    q = request.args.get('q')
    if q:
        trainer = sql_commands.query_trainer(q)
    else:
        trainer = sql_commands.get_trainers()
    return render_template('trainer.html', results=trainer)


@app.route('/classes', methods=['GET', 'POST'])  # display all trainers root
def classes():
    q = request.args.get('q')                   # search bar implementation
    if q:
        clas = sql_commands.query_class(q)
    else:
        clas = sql_commands.get_classes()
    return render_template('class.html', results=clas)


# member registration loop
@app.route('/register_member', methods=['GET', 'POST'])
def register_member():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        date_input = datetime.strptime(
            request.form['dinput'], '%Y-%m-%d')
        # date time function needs integers to work
        # get the ints from the date time function
        year = int(date_input.year)
        month = int(date_input.month)
        day = int(date_input.day)

        height = request.form['height']
        weight = request.form['weight']

        sql_commands.create_member(
            username, password, firstname, lastname, year, month, day, height, weight)
        return redirect(url_for('members'))  # references name of function ^

    return render_template('register_member.html')


@app.route('/delete/<string:username>', methods=['GET', 'POST'])
def delete(username):
    sql_commands.delete_member(username)
    return redirect(url_for('members'))


if __name__ == '__main__':
    app.run(debug=True)
