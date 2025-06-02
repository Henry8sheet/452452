from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    'student01': '123456',
    'student02': 'abcdef'
}

user_schedules = {}

@app.route('/')
def default():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if userid in users and users[userid] == password:
            session['user'] = userid
            return redirect(url_for('schedule'))
        return "登入失敗"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if 'user' not in session:
        return redirect(url_for('login'))

    user = session['user']

    if request.method == 'POST':
        schedule = []
        for i in range(5):
            row = []
            for j in range(5):
                cell_name = f"cell_{i}_{j}"
                value = request.form.get(cell_name, "")
                row.append(value)
            schedule.append(row)
        user_schedules[user] = schedule
        return redirect(url_for('schedule'))

    schedule = user_schedules.get(user, [["" for _ in range(5)] for _ in range(5)])
    return render_template('schedule.html', user=user, schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
