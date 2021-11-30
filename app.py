from flask import Flask, render_template, url_for, request, redirect, session, flash
import sql_commands
from datetime import datetime


app = Flask(__name__)
app.secret_key = "#244!2fcvdf1!"  # Session key


@app.route('/')
@app.route('/home')     # home root
def home_page():
    return render_template('home.html')


@app.route('/member', methods=['GET', 'POST'])
def members():
    if "admin" in session:
        q = request.args.get('q')
        if q:
            members = sql_commands.query_member(q)
        else:
            members = sql_commands.get_members()
        return render_template('member.html', results=members)
    else:
        return render_template('home.html')


@app.route('/trainer', methods=['GET', 'POST'])  # display all trainers root
def trainers():
    if "admin" in session:
        q = request.args.get('q')
        if q:
            trainer = sql_commands.query_trainer(q)
        else:
            trainer = sql_commands.get_trainers()
        return render_template('trainer.html', results=trainer)
    else:
        return render_template('home.html')


@app.route('/member_register/<string:clas>', methods=['GET', 'POST'])
def member_register(clas):
    sql_commands.member_register(session["user"], clas)
    return redirect(url_for('schedule'))


@app.route('/trainer_register/<string:username>', methods=['GET', 'POST'])
def trainer_register(username):
    sql_commands.trainer_register(session["admin"], username)
    return redirect(url_for('schedule'))


@app.route('/classes', methods=['GET', 'POST'])  # display all trainers root
def classes():
    rClasses = ""
    q = request.args.get('q')                    # search bar implementation
    if q:
        clas = sql_commands.query_class(q)
    else:
        clas = sql_commands.get_classes()

    if "user" in session:
        clas = [item for item in clas if item[4] > 0]
        rClasses = sql_commands.get_registered_ids(session["user"])
        rClasses = [item[0] for item in rClasses]
        clas = [list(item) for item in clas if item[0] not in rClasses]
    else:
        clas = [list(item) for item in clas]

    for row in clas:
        if row[1] is not None:
            row[1] = sql_commands.get_trainer_name(row[1])[0]

    return render_template('class.html', results=clas)


@app.route('/member_drop_class/<string:clas>', methods=['GET', 'POST'])
def member_drop_class(clas):
    sql_commands.member_drop_class(session["user"], clas)
    return redirect(url_for('schedule'))


@app.route('/trainer_drop_class/<string:clas>', methods=['GET', 'POST'])
def trainer_drop_class(clas):
    sql_commands.trainer_drop_class(session["admin"], clas)
    return redirect(url_for('schedule'))


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if "user" in session:
        clas = sql_commands.get_registered_classes(session["user"])
    elif "admin" in session:
        clas = sql_commands.get_trainer_classes(session["admin"])
    return render_template('schedule.html', results=clas)

@app.route('/member_count', methods=['GET', 'POST'])
def member_count():
    data = sql_commands.member_count_view()
    return render_template('member_count.html', results=data)


@app.route('/delete/<string:username>', methods=['GET', 'POST'])
def delete(username):
    sql_commands.delete_member(username)
    return redirect(url_for('members'))


@app.route('/register_member', methods=['GET', 'POST'])
def register_member():
    if session:
        return render_template('home.html')
    else:
        if request.method == 'POST':
            try:
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

                eval = sql_commands.create_member(
                    username, password, firstname, lastname, year, month, day, height, weight)
            except:
                flash("Invalid Input, Please Try Again", category="danger")
                return redirect(url_for('register_member'))

            if(eval):
                flash("Successfully registered!", category="info")
                # references name of function ^
                return redirect(url_for('login'))
            else:
                flash("Invalid Input, Please Try Again", category="info")
                return redirect(url_for('register_member'))

        return render_template('register_member.html')


@app.route('/delete_trainer/<string:username>', methods=['GET', 'POST'])
def delete_trainer(username):
    sql_commands.delete_trainer(username)
    return redirect(url_for('trainers'))


@app.route('/register_trainer', methods=['GET', 'POST'])
def register_trainer():
    if session:
        return render_template('home.html')
    else:
        if request.method == 'POST':
            try:
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

                eval = sql_commands.create_trainer(
                    username, password, firstname, lastname, year, month, day)
            except:
                flash("Invalid Input, Please Try Again", category="danger")
                return redirect(url_for('register_trainer'))

            if(eval):
                # references name of function ^
                return redirect(url_for('login'))
            else:
                flash("Invalid Input, Please Try Again", category="info")
                return redirect(url_for('register_trainer'))

        return render_template('register_trainer.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = sql_commands.get_member(username)

        if(user):
            if(user[0][1] == password):
                session["user"] = user[0][0]
                session["name"] = user[0][2]
                return redirect(url_for("home_page"))
            else:
                flash("Invalid Password", category="danger")
        else:
            user = sql_commands.get_trainer(username)
            if(user):
                if(user[0][1] == password):
                    session["admin"] = user[0][0]
                    session["name"] = user[0][2]
                    return redirect(url_for("home_page"))
                else:
                    flash("Invalid Password", category="danger")
            else:
                flash("Something Went Wrong, Please Try Again", category="info")
                return redirect(url_for("login"))

    return render_template('login_page.html')


@app.route("/logout")
def logout():
    if "user" in session:
        flash("You have been logged out!", category="info")
    session.pop("user", None)
    session.pop("admin", None)
    session.pop("name", None)
    return redirect(url_for("login"))



if __name__ == '__main__':
    app.run(debug=True)
