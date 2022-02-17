"""
自定义转换器
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义转换器
class RegexConverter(BaseConverter):

    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        return value


# 将自定义的转换器类添加到flask应用中
app.url_map.converters['re'] = RegexConverter


@app.route('/index/<re("123"):val>')
def index(val):
    return 'hello python'


if __name__ == '__main__':
    app.run()
