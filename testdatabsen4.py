import sqlite3
conn = sqlite3.connect('testDB.db')
query ='INSERT INTO Company (Name, Age, Address, Salary)VALUES(?,?,?,?)'
data = ('Dan Brown', 33, 'guldbergsgade 29N', 34000.00)
try:
    cur = conn.cursor()
    cur.execute(query, data)
    rowid = cur.lastrowid
 # Auto incremented/assigned id
    print(f'id of last row insert = {rowid}')
    conn.commit()
except sqlite3.Error as e:
    conn.rollback()
    print(f'Could not insert into Company! {e}')
finally:
    conn.close()
