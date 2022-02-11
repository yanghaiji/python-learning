"""
datetime 模块提供了以简单和复杂的方式操作日期和时间的类。
虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。
该模块还支持可感知时区的对象。
"""

from datetime import date
from datetime import datetime, timedelta

now = date.today()
print(now)
print(now.strftime('%a, %b %d %H:%M'))
date.isoweekday()

datetime.now().date()

datetime.today()
datetime.now().timestamp()
# 用指定日期时间创建datetime
datetime(2022, 2, 11, 12, 20)

cday = datetime.strptime('2022-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

now - timedelta(days=1)
