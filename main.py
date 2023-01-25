import os
import sys
import bottle
import sqlite3
from bottle import default_app, redirect, route, template, static_file, run, debug



if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

@route('/cars')
def show_json():
    return '<h1> TAHUBULAT</h1>' + template('db/cars.json')

@bottle.route('/db/<filename:re:.*\.JSON>')
def send_json(filename):
    return static_file(filename, root='./db')

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return default_app()

if __name__ == '__main__':
    # Starts a local test server.
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    
    bottle.run(server='wsgiref', host='localhost', port=PORT)