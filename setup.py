#!/usr/bin/env python


import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 6):
    raise SystemExit('ERROR: Barman Api needs at least python 2.6 to work')

install_requires = [
    'flask-restful',
    'Flask-HTTPAuth',
    'Flask-Script',
    'Flask-Login',
    'pyjwt'
]

barman_api = {}
with open('barmanui/version.py', 'r') as f_version:
    exec (f_version.read(), barman_api)

setup(
    name='barmanui',
    version=barman_api['__version__'],
    author='Mehmet Emin KARAKAS',
    author_email='emin100@gmail.com',
    url='https://github.com/emin100/barmanui',
    keywords="barmanui Rest api barman",
    packages=['barmanui', ],
    scripts=['bin/barmanui', ],
    license='GPL-3.0',
    description='This project convert from BARMAN command to RESTful api. Barman API support full future and all versions of BARMAN.',
    long_description='This project convert from BARMAN command to RESTful api. Barman API support full future and all versions of BARMAN.',
    install_requires=install_requires,
    platforms=['Linux', 'Mac OS X'],
    data_files=[
        ('/etc/', ['config/barmanui.conf']),
        ('/usr/share/barmanui/', ['config/client.conf']),
        ('/usr/share/barmanui/', ['config/man.conf']),
        ('/usr/share/barmanui/template/', ['config/template/config_change_template']),
    ],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: Database',
        'Topic :: System :: Recovery Tools',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Flask',
        'Natural Language :: English',
    ],
)
