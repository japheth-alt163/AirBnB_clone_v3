#!/usr/bin/python3
"""Defines views for State objects handling RESTful API actions."""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage, State


@app_views.route('/states', methods=['GET'])
def get_states():
    """Retrieves the list of all State objects."""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states]), 200


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieves a State object."""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict()), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """Creates a State."""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a State object."""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object."""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200
