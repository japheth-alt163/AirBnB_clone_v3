#!/usr/bin/python3
"""starts the Flask Airbnb clone
web application"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """handles @app.teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """returns a JSON-formatted 404
    status code response"""
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
