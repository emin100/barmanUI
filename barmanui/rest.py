import requests

from flask import current_app, flash


class Rest(object):
    api_config = None
    url = None

    def __init__(self):
        self.api_config = current_app.config.config_main.read_section('barmanapi')
        self.url = 'http://' + self.api_config.get('user') + ':' + self.api_config.get(
            'password') + '@' + self.api_config.get(
            'url')

    def get_token(self):
        r = requests.get(self.url + '/auth/token').json()
        return r.get('token')

    def get(self, uri):
        try:
            r = requests.get(self.url + uri)
            return r.json()
        except:
            flash('Test', 'error')
        return {}

    def get_with_token(self, uri, params=''):
        try:
            r = requests.get(self.url + uri + '?token=' + str(self.get_token())+'&'+params)
            return r.json()
        except:
            flash('Test', 'error')
        return {}
