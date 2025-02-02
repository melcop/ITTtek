import sqlite3

# Opret forbindelse til databasen
conn = sqlite3.connect("testDB.db")
cursor = conn.cursor()

# Indsæt data én ad gangen
cursor.execute("INSERT INTO COMPANY (name, age, address, salary) VALUES ('Paul', 32, 'California', 20000.00);")
cursor.execute("INSERT INTO COMPANY (name, age, address, salary) VALUES ('Allen', 25, 'Texas', 15000.00);")
cursor.execute("INSERT INTO COMPANY (name, age, address, salary) VALUES ('Teddy', 23, 'Norway', 20000.00);")
cursor.execute("INSERT INTO COMPANY (name, age, address, salary) VALUES ('James', 24, 'Houston', 10000.00);")

# Gem ændringer og luk forbindelsen
conn.commit()
conn.close()

print("Data inserted into COMPANY table in testDB.db!")