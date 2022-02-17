from flask import Flask

app = Flask(__name__)


# 根据id查询
# 参数类型默认是string
@app.route('/user/<id>')
def get_user(id):
    if id == '1':
        return 'admin'
    elif id == '2':
        return 'guest'
    else:
        return 'not found'


# 参数类型默认是string
# 可以指定参数类型
@app.route('/user/int/<int:id>')
def get_user(id):
    if id == 1:
        return 'admin'
    elif id == 2:
        return 'guest'
    else:
        return 'not found'


if __name__ == '__main__':
    app.run()
