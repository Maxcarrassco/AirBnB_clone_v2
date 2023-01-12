#!/usr/bin/python3
"""ALX SE FLASK Module."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Return 'Hello HBNB!' when our root url is access."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return 'HBNB!' when our root url is access."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Return 'C + var text value' when our root url is access."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is cool'):
    """Return 'Python + text value or is cool' when our root url is access."""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
