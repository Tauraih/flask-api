import time
import logging
from flask import Flask
from flask import json

app = Flask(__name__)


logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route("/")
def hello():
    return {"msg": "Hello World!"}


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({'user': 'admin', 'result': 'OK - health'}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('%s, s endpoint was reached', response)
    return response


@app.route("/metrics")
def get_metrics():
    data = {'UserCount': 140, 'UserCountActive': 23}
    app.logger.info('%s, s endpoint was reached', data)
    return {"user": "admin", 'data': data}, 200


@app.route('/time')
def get_curent_time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(host='0.0.0.0')