#!/usr/bin/python3
"""Defines unit tests for City views."""

import unittest
from unittest.mock import patch
from io import StringIO
from flask import Flask, jsonify
from api.v1.app import app
from models import storage
from models.state import State
from models.city import City


class TestCitiesView(unittest.TestCase):
    """Test cases for cities view."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Reset storage."""
        storage.delete_all()
        storage.save()

    def test_get_cities_of_state(self):
        """Test retrieving all City objects of a State."""
        # Create a State and City
        state = State(name="Test State")
        storage.new(state)
        storage.save()
        city = City(name="Test City", state_id=state.id)
        storage.new(city)
        storage.save()
        
        # Send GET request to /states/<state_id>/cities
        response = self.app.get(f'/api/v1/states/{state.id}/cities')
        
        # Check response status code and content
        self.assertEqual(response.status_code, 200)
        cities_data = response.get_json()
        self.assertEqual(len(cities_data), 1)
        self.assertEqual(cities_data[0]['name'], "Test City")

    # Add more test cases for other endpoints...


if __name__ == '__main__':
    unittest.main()
