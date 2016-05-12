from ConfigParser import ConfigParser as Parser

from baseexception import BaseBarmanUIException
import os


class ConfigParser(Parser):
    path = None

    def __init__(self, filename=None, io=None):
        Parser.__init__(self)
        if io is None:
            if filename is None:
                raise IOError('Config File Is Empty')
            if os.path.exists(filename):
                self.path = filename
            elif os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/' + filename):
                self.path = os.path.dirname(os.path.realpath(__file__)) + '/' + filename
            else:
                raise ConfigParserException('Config File Not Found', 404, ConfigParserException.NOT_FOUND)
            self.read(self.path)
        else:
            if io is None:
                raise IOError('Config File and Io Is Empty')
            self.readfp(io)

    def write_config(self):

        with open(self.path, 'wb') as configfile:
            self.write(configfile)

    def read_section(self, name):
        dict1 = {}
        try:
            options = self.options(name)
            for option in options:
                try:
                    dict1[option] = self.get(name, option)
                    if dict1[option] == -1:
                        print("skip: %s" % option)
                except:
                    print("exception on %s!" % option)
                    dict1[option] = None
        except:
            raise ConfigParserException('Section Not Found', 404, ConfigParserException.NOT_FOUND)
        return dict1


class ConfigParserException(BaseBarmanUIException):
    pass
