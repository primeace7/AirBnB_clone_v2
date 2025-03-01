#!/usr/bin/python3

'''
Start a flask app that listens on 0.0.0.0 and returns responses for four
routes: /, /hbnb, /c/<text>, and /python/<text>
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_cool(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run()
