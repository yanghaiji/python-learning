
import sqlite3


conn_select = sqlite3.connect('python_learning.db')
cursor_select = conn_select.cursor()
# 执行查询语句:
cursor_select.execute('select * from user ')

# 获得查询结果集:
values = cursor_select.fetchall()
print(values)
cursor_select.close()
conn_select.close()
