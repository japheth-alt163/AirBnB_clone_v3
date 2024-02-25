#!/usr/bin/python3
"""
Module: states
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage, State


def check_state(state_id):
    """Helper function to retrieve a State object by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return state


@app_views.route('/states', methods=['GET'])
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieves a State object by id"""
    state = check_state(state_id)
    return jsonify(state.to_dict())


@app_views.route('/states', methods=['POST'])
def create_state():
    """Creates a State object"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a State object by id"""
    state = check_state(state_id)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ('id', 'created_at', 'updated_at'):
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object by id"""
    state = check_state(state_id)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
