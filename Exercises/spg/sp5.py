# importerer sqlite3 modulet
import sqlite3
# laver et connection objekt som refereres til med variablen conn og forbinder til
# eller opretter databasen test_database.db
conn = sqlite3.connect('test_database.db') 
# laver et cursor objekt som kaldes c  - kunne kaldes curs
c = conn.cursor()
# starter try blok for at undgå at programmet crasher hvis der opstår en fejl 
try:
    # execute sørger for at sql bliver eksekveret til databasen
    c.execute(
        # laver en table kaldet products hvis den ikke findes i forvejen
        # der er 3 felter i databasen
        # product_id er et heltal og primary KEY (som er unikt) - Har ikke autoincrement eller NOTT NULL
        # [kollonne navne] 
        '''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY,
           [product_name] TEXT, [price] INTEGER)
          ''')                                          
    c.execute(
        # der anvendes INSERT INTO statement og,
        # indsætter 5 rows  i tabellen products hvor der gives data til kolonnerne med med id, navn og pris, 
        '''
            INSERT INTO products (product_id, product_name, price)
                    VALUES
                    (1,'Computer', 800),
                    (2,'Printer', 200),
                    (3,'Tablet', 300),
                    (4,'Desk', 450),
                    (5,'Chair', 150)
            ''')
    # gem ændringerne som er blevet eksekveret i databasen
    conn.commit()

    c.execute(
        # bruger SELECT statement til at vælge alle * fra products tabellen hvor prisen er under 400
        '''
          SELECT * FROM products WHERE price < 400;
          ''')
    # for at hente data efter SELECT statement kan fetchall metoden kaldes
    # som returnerer en liste med alle rows fra SELECT querien.
    # rows opbevares som tuples i listen
    rset = c.fetchall()
    # Printer længden på listen rset
    print(f'Row-count : { len(rset) } \n List : {rset} ')
    # for loop der itererer over listen rset
    for row in rset:
        # print med f-string der viser elementerne i listen på plads 1 og 2 som er navn og pris
        print(f'name={row[1]} price={row[2]}  \n')
# except statement der giver en generel fejledelelse fra sqlite3.Error
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"')
# finally statement som eksekveres ligegyldigt hvad der sker
finally:
    # lukker forbindelsen til databasen
    conn.close()