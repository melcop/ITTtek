import sqlite3
conn = sqlite3.connect('testDB.db')
try:
    cur = conn.cursor()
    cur.execute('SELECT * FROM COMPANY')
    rset = cur.fetchall()
    print(f'Row-count : { len(rset) } ')
    for row in rset:
        print(f'name={row[1]}')
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"')
finally:
    conn.close()