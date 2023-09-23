#!/usr/bin/python3

'''
create a route that lists all the cities in a state in the /states_list route
'''

from flask import Flask
from flask import render_template
from ../models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_storage():
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    return render_template('7-states_list.html', storage=storage.all(States))


if __name__ == '__main__':
    app.run()
