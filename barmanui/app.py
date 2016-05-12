from flask import Flask, render_template
from flask.ext.login import LoginManager, login_required
from flask.ext.restful import Api
from flask.ext.script import Manager
from auth import User
from parser import ConfigParser

app = Flask(__name__, instance_relative_config=True)
api = Api(app)
manager = Manager(app)
login_manager = LoginManager()
login_manager.init_app(app)
config_main = ConfigParser('/etc/barmanui.conf')


@login_manager.user_loader
def load_user(user_id):
    return User.get()


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('login.html')


# auth_token = HTTPTokenAuth(scheme='Barman')


# class Auth(AuthBase):
#     decorators = [auth_token.login_required]
#     pass
#
#
# api.add_resource(Auth, '/auth/<command>', methods=['GET', 'POST'])


@app.route("/")
@login_required
def hello():
    return render_template('index.html')


@manager.command
def runserver():
    """Start BARMAN API Server"""

    app.run(debug=True)


def main():
    manager.run()


if __name__ == '__main__':
    manager.run()
