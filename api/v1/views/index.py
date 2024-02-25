#!/usr/bin/python3

"""Index module that contains
the routes for API statistics."""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Retrieve statistics of the
    number of objects for each type."""
    return jsonify(status="OK")
