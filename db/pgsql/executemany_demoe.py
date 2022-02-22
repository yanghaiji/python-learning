import psycopg2

"""
executemany()方法是一种方便的方法，用于针对在提供的序列中找到的所有参数元组或映射启动数据库操作（查询或命令）。
 该函数对更新数据库的命令最有用：查询返回的任何结果集都将被丢弃。
"""
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

con = psycopg2.connect(database='testdb', user='postgres',
                       password='s$cret')

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")

    query = "INSERT INTO cars (id, name, price) VALUES (%s, %s, %s)"
    cur.executemany(query, cars)

    con.commit()
