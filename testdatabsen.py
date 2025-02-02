import sqlite3

conn = sqlite3.connect('testDB.db')
try:
    cur = conn.cursor()
    cur.execute('SELECT * FROM COMPANY Limit 3')
    for row in cur:
        print(f'id ={row[0]:2d} salary={row[4]}')
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"')
finally:
    conn.close() # Close connection to server