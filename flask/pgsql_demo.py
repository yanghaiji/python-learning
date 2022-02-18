"""
python 连接pgsql
如果您没有下载 sqlalchemy psycopg2 可以执行install.sh里的命令
"""
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# 其中user表示数据库的用户，password表示连接数据库的密码，hostname可以用localhost(其他的写ip即可，port如果不是默认端口，需要指定)，
# databasee_name用你连接的数据库的名字，以下是一个示例：
engine = create_engine('postgresql+psycopg2://user:password@localhost:port/databasee_name')
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)


@app.route('/user')
def query():
    users = db.execute("SELECT * FROM sys_user").fetchall()
    payload = []
    content = {}
    for result in users:
        content = {'id': result[0], 'username': result[1], 'password': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)


if __name__ == "__main__":
    app.run()
