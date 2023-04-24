from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from login import login_user

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            return redirect(url_for('success'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
