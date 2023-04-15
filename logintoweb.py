import sqlite3

# Opret forbindelse til databasen
conn = sqlite3.connect('users.db')

# Opret cursor objekt
c = conn.cursor()

# Opret tabel
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

# Indsæt data i tabellen
c.execute("INSERT INTO users VALUES ('user1', 'password1')")
c.execute("INSERT INTO users VALUES ('user2', 'password2')")
c.execute("INSERT INTO users VALUES ('user3', 'password3')")

# Gem ændringerne i databasen
conn.commit()

# Funktion til at validere brugernavn og password
def validate_login(username, password):
    # Udfør SELECT forespørgsel på databasen
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        return True
    else:
        return False

# Test login funktionen
print(validate_login('user1', 'password1'))  # Output: True
print(validate_login('user2', 'password3'))  # Output: False

# Luk forbindelsen til databasen
conn.close()
