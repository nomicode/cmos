from flask import Flask, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {'testuser': 'password'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('protected'))
        return 'Invalid credentials', 401
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/protected')
def protected():
    if 'username' in session:
        return f'Hello, {session["username"]}!'
    return 'You are not logged in', 401

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/404')
def not_found():
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(port=5000)
