

from flask import Flask, render_template,request
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
    return User.get(user_id)


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


@app.route("/login", methods=['POST'])
def login():
    password = request.form.get('inputPassword')
    username = request.form.get('inputUsername')
    user = User.get(username,password)

    # user = User.query.get(form.email.data)
    # if user:
    #     if bcrypt.check_password_hash(user.password, form.password.data):
    #         user.authenticated = True
    #         db.session.add(user)
    #         db.session.commit()
    #         login_user(user, remember=True)
    #         return redirect(url_for("bull.reports"))

    return 'dfdssdf'


@app.route("/logout")
def logout():
    pass


@manager.command
def runserver():
    """Start BARMAN API Server"""

    app.run(debug=True)


def main():
    manager.run()


if __name__ == '__main__':
    manager.run()
