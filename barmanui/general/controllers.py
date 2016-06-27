from flask import Blueprint, render_template
from flask_login import login_required

general = Blueprint('general', __name__, url_prefix='/')


@general.route("/")
@login_required
def hello():
    return render_template('index.html')
