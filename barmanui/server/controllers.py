from flask import Blueprint, render_template, flash
from flask.ext.login import login_required

from general.models import Rest

server = Blueprint('server', __name__, url_prefix='/server')


@server.route("/")
@login_required
def server_list():
    rest = Rest()
    list_server = rest.get_with_token('/barman/list-server')
    print list_server

    list_return = []
    if list_server.get('status_code') == 200:
        list_send = list_server.get('list')
        i = 0
        for message in list_send:
            if message != '':
                message = message.split(' - ')
                list_return.append({'name': message[0], 'desc': message[1], 'settings': [
                    {'icon': 'stats', 'target': '/server/status'}]})
                i += 1
    else:
        flash(list_server.get('message'), 'error')
    return render_template('list.html', list=list_return, panel_header='Server List',
                           table_header=['Name', 'Description', '#'], order=['name', 'desc', 'settings'])
