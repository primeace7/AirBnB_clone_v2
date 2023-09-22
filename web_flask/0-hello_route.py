#!/usr/bin/python3

'''
A simple flask application that listens on 0.0.0.0 port 5000
'''

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def helllo():
    return f'Hello HBNB!'

if __name__ == '__main__':
    app.run()
