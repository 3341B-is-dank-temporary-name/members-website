"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, current_app, jsonify
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

import json

@app.route('/')
def index():
    # Load 3341b info
    with current_app.open_resource("3341b_info.json") as f:
        info = json.load(f)

    return render_template("index.html", info=info)

@app.route("/json")
def raw_json():
    # Load 3341b info
    with current_app.open_resource("3341b_info.json") as f:
        info = json.load(f)
    return jsonify(info=info)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
