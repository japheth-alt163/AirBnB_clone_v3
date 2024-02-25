# api/v1/views/index.py
"""Index module that contains the routes for API statistics."""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Retrieve statistics of the number of objects for each type."""
    stats = {
        "status": "OK"
    }
    return jsonify(stats)
