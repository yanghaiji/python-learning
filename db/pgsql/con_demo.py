import psycopg2
import sys

con = psycopg2.connect(database='testdb', user='postgres',
                       password='s$cret')
with con:
    cur = con.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()[0]
    print(version)
    
"""
try:
    con = psycopg2.connect(database='testdb', user='postgres',
                           password='s$cret')
    cur = con.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()[0]
    print(version)
except psycopg2.DatabaseError as e:
    print(f'Error {e}')
    sys.exit(1)
finally:
    if con:
        con.close()

"""
