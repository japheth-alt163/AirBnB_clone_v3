#!/usr/bin/python3
"""Initialize the Blueprint for views."""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the routes
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.cities import *  # Add this line to import the cities routes
from api.v1.views.users import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
