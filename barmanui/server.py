from rest import Rest
from flask import request, render_template


class Server(Rest):
    def get_command(self, command):
        server_command = self.get_with_token('/barman/' + command, 'SERVER_NAME=' + request.args.get('SERVER_NAME'))
        print server_command

    def server_list(self):
        server_list = self.get_with_token('/barman/list-server')
        if server_list.get('code') > 0:
            print 'Hata'
        else:
            return_list = []
            list_send = server_list.get('message')
            i = 0
            for message in list_send:
                if message != '':
                    message = message.split(' - ')
                    return_list.append({'name': message[0], 'desc': message[1], 'settings': [
                        {'icon': 'stats', 'target': '/server/status'}]})
                    i += 1

        return render_template('list.html', list=return_list, panel_header='Server List',
                               table_header=['Name', 'Description', '#'])
