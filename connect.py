import sqlite3
try:
    conn = sqlite3.connect(database='testDB.db')
    print("Det virker!")
# Se PEP249
except sqlite3.OperationalError as oe:
    print(f'Transaction could not be processed : { oe }')
except sqlite3.IntegrityError as ie:
    print(f'Integrity constraint violated : { ie }')
except sqlite3.ProgrammingError as pe:
    print(f'You used the wrong SQL table : { pe }')
except:
    print('Some other mishap occurred')