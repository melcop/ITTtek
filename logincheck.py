import sqlite3

def check_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

username = input("Indtast username: ")
password = input("Indtast password: ")

if check_login(username, password):
    print("Login succesfuldt")
else:
    print("Login mislykkedes")