#!/usr/bin/python3
"""ALX SE Flask Module."""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_state():
    """Render list of all states and cities link to them."""
    states_list = storage.all(State)
    return render_template('8-cities_by_states.html', states=states_list)


@app.teardown_appcontext
def close_session(exception=None):
    """Close the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
