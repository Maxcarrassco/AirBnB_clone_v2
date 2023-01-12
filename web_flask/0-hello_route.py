#!/usr/bin/python3
"""ALX SE FLASK Module."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Return 'Hello HBNB' when our root url is access."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
