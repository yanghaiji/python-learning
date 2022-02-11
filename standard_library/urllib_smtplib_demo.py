"""
有许多模块可用于访问互联网和处理互联网协议。
其中两个最简单的 urllib.request 用于从URL检索数据，以及 smtplib 用于发送邮件:
"""

from urllib.request import urlopen
import smtplib

# 打开网页
with urlopen('https://blog.csdn.net/weixin_38937840/article/details/122859206') as response:
    for line in response:
        print(line.decode())

# 邮件发送
server = smtplib.SMTP('localhost')
server.sendmail('222@qq.com', '222@qq.com', 'hello python')
server.quit()
