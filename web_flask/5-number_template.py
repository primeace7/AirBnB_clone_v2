#!/usr/bin/python3

'''
Start a flask app that listens on 0.0.0.0 and returns responses for six
routes: /, /hbnb, /c/<text>, /python/<text>, /number/<n>, and
/number_template/<n>
'''

from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number(n):
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run()
