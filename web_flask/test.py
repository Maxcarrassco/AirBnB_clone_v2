from flask import Flask, url_for


app = Flask(__name__)

@app.route('/come')
def home():
    return "OK"

with app.test_request_context():
    print(url_for('home', next='go', name='max'))
