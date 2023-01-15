#!/usr/bin/python3
"""ALX SE Flask Module."""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """Render list of all states."""
    states_list = storage.all(State)
    return render_template('7-states_list.html', states=dict(sorted(
        states_list.items(), key=lambda x: x[1].name)))


@app.teardown_appcontext
def close_session(exception):
    """Close the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
