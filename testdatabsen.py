import sqlite3

conn = sqlite3.connect('testDB.db')
try:
    cur = conn.cursor()
    cur.execute('SELECT * FROM COMPANY Limit 2')
    for row in cur:
        print(row)
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"')
finally:
    conn.close() # Close connection to server