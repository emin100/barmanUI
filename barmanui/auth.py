from flask import flash
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
        remember = False
        if request.form.get('remember_me') == 'on':
            remember = True
        login_user(user, remember=remember)
        rest = Rest()
        user.other = rest.get('/auth/user')
        # login_user(user, remember=remember)
        if user.other.get('message'):
            flash(user.other.get('message'), 'error')
            logout_user()

    @staticmethod
    def logout():
        logout_user()


class User(UserMixin):
    id = None
    username = None
    password = None
    other = {}

    def get_id(self):
        return [self.username, self.password]

    def get(self, id):
        self.username = id[0]
        self.password = id[1]
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
