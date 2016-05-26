from flask.ext.login import UserMixin


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