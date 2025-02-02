import sqlite3

# Opret en forbindelse til databasen (eller opret den, hvis den ikke findes)
conn = sqlite3.connect("testDB.db")

# Opret en cursor
cursor = conn.cursor()

# Opret tabellen COMPANY
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DEPARTMENT (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dept CHAR(50) NOT NULL,
        emp_id INT NOT NULL
    )
''')

# Gem ændringer og luk forbindelsen
conn.commit()
conn.close()

print("Tabellen DEPARTMENT er oprettet i testDB.db!")