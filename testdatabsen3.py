import sqlite3
conn = sqlite3.connect('testDB.db')
sql = """INSERT INTO Company (NAME, AGE, ADDRESS, SALARY) VALUES('Lars Larsen', 55, 'Lygten 16', 99999.00)"""
try:
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
except sqlite3.Error as e:
    conn.rollback()
    print(f'Could not insert ! {e}')
finally:
    conn.close() # Close connection to server