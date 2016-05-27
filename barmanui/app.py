from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.script import Manager

from auth.models import User
from parser import ConfigParser


from auth.controllers import mod_auth as auth_module
from general.controllers import general
from server.controllers import server

app = Flask(__name__)
app.secret_key = 'super secret key'
manager = Manager(app)
Bootstrap(app)

app.config.config_main = ConfigParser('/etc/barmanui.conf')


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(general)
app.register_blueprint(server)

login_manager = LoginManager()
login_manager.init_app(app)
app.config.config_main = ConfigParser('/etc/barmanui.conf')


@login_manager.user_loader
def load_user(user_id):
    return User().get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('login.html', request=request)


@manager.command
def runserver():
    """Start BARMAN UI Server"""

    app.run(debug=True)


def main():
    manager.run()


if __name__ == '__main__':
    manager.run()

'''
from flask import Flask, render_template, request, redirect, g
from flask.ext.login import LoginManager, login_required, current_user
from flask.ext.restful import Api
from flask.ext.script import Manager

from auth import User, AuthBase
from server import Server
from rest import Rest
from parser import ConfigParser

app = Flask(__name__, instance_relative_config=True)

app.secret_key = 'super secret key'
manager = Manager(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.config_main = ConfigParser('/etc/barmanui.conf')


# @app.before_request
# def before_request():
#     print current_user.username
#     g.user = current_user


@login_manager.user_loader
def load_user(user_id):
    return User().get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('login.html', request=request)


@app.route("/")
@login_required
def hello():
    return render_template('index.html')


class ServerApi(Server):
    decorators = [login_required]
    pass
app.register_blueprint(ServerApi, url_prefix='/server')
# app.add_resource(ServerApi, '/server/<command>/<option>', '/server/<command>', '/server', methods=['GET', 'POST'])

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
'''
