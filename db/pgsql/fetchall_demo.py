"""
fetchall()获取查询结果的所有（剩余）行，并将它们作为元组列表返回。 如果没有更多记录可获取，则返回一个空列表。
"""
import psycopg2

con = psycopg2.connect(database='testdb', user='postgres',
                       password='s$cret')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM cars")
    # fetchone 逐行查询
    rows = cur.fetchall()

    for row in rows:
        print(f"{row[0]} {row[1]} {row[2]}")
