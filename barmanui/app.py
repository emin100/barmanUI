from flask import Flask, render_template, g, make_response, request, jsonify
from flask.ext.httpauth import HTTPTokenAuth, HTTPBasicAuth
from flask.ext.restful import Api
from flask.ext.script import Manager

app = Flask(__name__, instance_relative_config=True)
api = Api(app)
manager = Manager(app)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    return jsonify(ret_data)


@manager.command
def runserver():
    """Start BARMAN API Server"""

    app.run(debug=True)


def main():
    manager.run()


if __name__ == '__main__':
    manager.run()
