# 连接到SQLite数据库
# 数据库文件是python_learning.db
# 如果文件不存在，会自动在当前目录创建:
import sqlite3

conn = sqlite3.connect("python_learning.db")
cursor = conn.cursor()
# 创建表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
