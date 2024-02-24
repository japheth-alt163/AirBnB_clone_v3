# api/v1/views/index.py
"""Index module that contains the routes for API statistics."""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieve statistics of the number of objects for each type."""
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
