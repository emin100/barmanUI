from flask.ext.login import UserMixin

from baseexception import BaseBarmanUIException

from flask.ext.restful import Resource, request
from flask.ext.login import login_user, logout_user
from rest import Rest


class AuthBase(Resource):
    @staticmethod
    def login():
        password = request.form.get('inputPassword')
        username = request.form.get('inputUsername')
        user = User()
        user.username = username
        user.password = password
        rest = Rest()
        user.other = rest.get('/auth/user')
        remember = False
        if request.form.get('remember_me') == 'on':
            remember = True
        login_user(user, remember=remember)

    @staticmethod
    def logout():
        logout_user()


class User(UserMixin):
    id = None
    username = None
    password = None
    other = {}

    def get_id(self):
        return self.username

    def get(self):
        return self

    # Required for administrative interface
    def __unicode__(self):
        return self.username


class AuthException(BaseBarmanUIException):
    status_code = 401

    AUTH_ERROR = 'Authoratization Error'
    TOKEN_ERROR = 'Invalid Client Token'
    TOKEN_TIME_UP = 'Token time is up'
    ACCESS_DENY = 'Access deny for this rest'
    USER_FOUND = "Registered User"
