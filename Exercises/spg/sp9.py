import sqlite3

conn= sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS USERS
            (username text, password text)''')

c.execute("INSERT INTO users VALUES ('user1', 'passwood1')")
c.execute("INSERT INTO users VALUES ('user2', 'passwood2')")
c.execute("INSERT INTO users VALUES ('user3', 'passwood3')")

conn.commit()

def validate_login(username, password):

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
    
print(validate_login('user1', 'password1'))
print(validate_login('user2', 'password3'))
conn.close()