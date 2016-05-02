from flask import Flask, g, make_response, request
from flask.ext.httpauth import HTTPTokenAuth, HTTPBasicAuth
from flask.ext.restful import Api
from flask.ext.script import Manager




app = Flask(__name__, instance_relative_config=True)
api = Api(app)
manager = Manager(app)


def write_log(error_message, error_type):
    if hasattr(g, 'user'):
        message = ('User: %s ' % g.user.get('username'))
    else:
        message = ('User: %s ' % None)
    message += (str(error_type) + ': %s ' % (error_message))
    if request.url:
        message += ('Url: %s ' % request.url)
    if request.args:
        message += ('Arg: %s ' % request.args)
    app.logger.error(message)


@manager.command
def runserver():
    """Start BARMAN API Server"""

    app.run()


def main():
    manager.run()


if __name__ == '__main__':
    manager.run()