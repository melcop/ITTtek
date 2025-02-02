import sqlite3

# Opret en forbindelse til databasen (eller opret den, hvis den ikke findes)
conn = sqlite3.connect("testDB.db")

# Opret en cursor
cursor = conn.cursor()

# Opret tabellen COMPANY
cursor.execute('''
    CREATE TABLE IF NOT EXISTS COMPANY (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        address CHAR(50),
        salary REAL
    )
''')

# Gem ændringer og luk forbindelsen
conn.commit()
conn.close()

print("Tabellen COMPANY er oprettet i testDB.db!")