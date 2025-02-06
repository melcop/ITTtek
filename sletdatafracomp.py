import sqlite3
conn = sqlite3.connect('testDB.db')
try:
    cur = conn.cursor()
    cur.execute("DELETE FROM Company WHERE Name LIKE ?", ('d%',))
    conn.commit()
except sqlite3.Error as e:
    print(f'Unable to delete Name from database ! {e}')
finally:
    conn.close()