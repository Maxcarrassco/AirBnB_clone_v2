#!/usr/bin/python3
"""ALX SE Flask Module."""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Render list of all states."""
    states_list = storage.all(State)
    return render_template(
            '9-states.html', states=states_list, pass_with_id=False)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Render list of all states."""
    key = f'State.{id}'
    states_list = storage.all(State)
    state = states_list.get(key)
    return render_template('9-states.html', state=state, pass_with_id=True)


@app.teardown_appcontext
def close_session(exception=None):
    """Close the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
