from flask import Flask, jsonify, make_response, json

app = Flask(__name__)
# 使用jsonify时
app.config['JSON_AS_ASCII'] = False


@app.route('/jsonify')
def json_ify():
    data = {
        'name': '杨海吉'
    }
    return jsonify(data)


@app.route('/jsondumps')
def jsondumps():
    data = {
        'name': '杨海吉'
    }
    response = make_response(json.dumps(data, encoding='utf-8'))
    response.mimetype = 'application/json'
    return response


if __name__ == '__main__':
    app.run()
