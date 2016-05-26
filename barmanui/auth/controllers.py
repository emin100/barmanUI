# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask.ext.login import login_user, logout_user

from auth.models import User
from baseexception import BaseBarmanUIException

from general.models import Rest

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route("/logout")
def logout():
    logout_user()
    return redirect('/')


@mod_auth.route("/login", methods=['POST'])
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
    return redirect(request.form.get('request_url'))



class AuthException(BaseBarmanUIException):
    status_code = 401

    AUTH_ERROR = 'Authoratization Error'
    TOKEN_ERROR = 'Invalid Client Token'
    TOKEN_TIME_UP = 'Token time is up'
    ACCESS_DENY = 'Access deny for this rest'
    USER_FOUND = "Registered User"


