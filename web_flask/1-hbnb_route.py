#!/usr/bin/python3

'''
Start a flask app that listens on 0.0.0.0 and returns responses for two
routes: / and /hbnb
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


if __name__ == '__main__':
    app.run()
