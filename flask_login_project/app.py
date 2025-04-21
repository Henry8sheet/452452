from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    'student01': '123456',
    'student02': 'abcdef'
}

@app.route('/')
def default():
    return render_template('default.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if userid in users and users[userid] == password:
            session['user'] = userid
            return redirect(url_for('default'))
        return "登入失敗"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('default'))

if __name__ == '__main__':
    app.run(debug=True)
