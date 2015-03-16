#!\Python34\env Python
# -*- coding: <encoding utf-8> -*-  

"""
This script runs the Limonium application using a development server.
"""

from os import environ
from Limonium import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
