"""
默认游标检索元组中的数据。 使用字典光标，数据以 Python 字典的形式发送。 然后，我们可以通过列名称来引用数据。
"""
import psycopg2
import psycopg2.extras

con = psycopg2.connect(database='testdb', user='postgres',
                       password='s$cret')
with con:
    # 执行返回的类型为字典类型
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM cars")

    rows = cursor.fetchall()

    for row in rows:
        print(f"{row['id']} {row['name']} {row['price']}")
