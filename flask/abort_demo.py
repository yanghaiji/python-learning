"""
主动抛出异常
"""

from flask import Flask, abort, request

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        abort(401)
        return '123'
    else:
        abort(401)
        return None


# 自定义错误函数
@app.errorhandler(401)
def errorhandler_401(error):
    return '没有权限访问！'


if __name__ == '__main__':
    app.run()
