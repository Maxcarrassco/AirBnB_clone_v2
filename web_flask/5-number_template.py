#!/usr/bin/python3
"""ALX SE FLASK Module."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Return 'Hello HBNB!' when this route is access."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return 'HBNB!' when this route is access."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Return 'C + var text value' when this route is access."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is cool'):
    """Return 'Python + text value or is cool' when this route is access."""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Return 'var n value + is a number' when this route is access."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return a html page when this route is access."""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
