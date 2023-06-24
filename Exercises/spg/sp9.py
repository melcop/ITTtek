# Først importeres sqlite3-modulet.
import sqlite3

# Herefter oprettes forbindelse til en databasefil ved hjælp af sqlite3.connect('users.db').
# Hvis filen ikke eksisterer, oprettes den automatisk. Forbindelsen gemmes i variablen conn.
conn= sqlite3.connect('users.db')

# En cursor (peger) oprettes ved at kalde conn.cursor(), og denne cursor gemmes i variablen c.
# Cursor'en bruges til at udføre SQL-forespørgsler mod databasen.
c = conn.cursor()

# Derefter udføres en CREATE TABLE-forespørgsel ved at kalde c.execute() med den ønskede SQL-kommando. 
# I dette tilfælde oprettes en tabel kaldet "USERS" med to kolonner: "username" (tekst) og "password" (tekst).
# Hvis tabellen allerede eksisterer, ignoreres denne forespørgsel på grund af IF NOT EXISTS-klausulen.
c.execute('''CREATE TABLE IF NOT EXISTS USERS
            (username text, password text)''')

# Efter oprettelsen af tabellen udføres tre INSERT INTO-forespørgsler ved at kalde c.execute() med de ønskede SQL-kommandoer. 
# Disse forespørgsler indsætter rækker i "USERS"-tabellen med forskellige brugernavne og adgangskoder.
c.execute("INSERT INTO users VALUES ('user1', 'passwood1')")
c.execute("INSERT INTO users VALUES ('user2', 'passwood2')")
c.execute("INSERT INTO users VALUES ('user3', 'passwood3')")

# For at gemme ændringerne foretaget i databasen, kaldes conn.commit().
conn.commit()

# Derefter defineres en funktion ved navn validate_login(username, password). 
# Denne funktion bruger c.execute() til at udføre en SELECT-forespørgsel for at kontrollere, 
# om der findes en række i "USERS"-tabellen, der matcher det angivne brugernavn og adgangskode. 
# Hvis en matchende række findes, returneres True, ellers returneres False.
def validate_login(username, password):

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
    
# Til sidst kaldes validate_login() med forskellige brugernavne og adgangskoder, og resultatet bliver udskrevet ved hjælp af print().   
print(validate_login('user1', 'password1'))
print(validate_login('user2', 'password3'))

# Når alt er færdigt, lukkes forbindelsen til databasen ved at kalde conn.close(). 
# Dette frigiver ressourcer og lukker forbindelsen til databasen.
conn.close()