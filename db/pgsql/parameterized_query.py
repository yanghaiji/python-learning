"""
参数化

"""

import psycopg2

con = psycopg2.connect(database='testdb', user='postgres',
                       password='s$cret')

uId = 1
uPrice = 62300

con = psycopg2.connect(database='testdb', user='postgres',
                       password='s$cret')

with con:
    cur = con.cursor()
    cur.execute("UPDATE cars SET price=%s WHERE id=%s", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
