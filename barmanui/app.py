from flask import Flask, render_template, request, redirect
from flask.ext.login import LoginManager, login_required, login_user, logout_user
from flask.ext.restful import Api
from flask.ext.script import Manager

from auth import User, AuthBase
from server import Server
from rest import Rest
from parser import ConfigParser

app = Flask(__name__, instance_relative_config=True)
api = Api(app)
app.secret_key = 'super secret key'
manager = Manager(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.config_main = ConfigParser('/etc/barmanui.conf')


@login_manager.user_loader
def load_user(user_id):
    return User().get()


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('login.html', request=request)


@app.route("/")
@login_required
def hello():
    return render_template('index.html')


@app.route("/server")
@login_required
def server():
    server = Server()
    return server.server_list()


@app.route("/server/<command>")
@login_required
def server_command(command):
    server = Server()
    server.get_command(command)
    return render_template('list.html', list=Server().server_list())


@app.route("/logout")
def logout():
    AuthBase.logout()
    return redirect('/')


@app.route("/login", methods=['POST'])
def login():
    AuthBase.login()
    return redirect(request.form.get('request_url'))


@manager.command
def runserver():
    """Start BARMAN API Server"""

    app.run(debug=True)


def main():
    manager.run()


if __name__ == '__main__':
    manager.run()
