#!/usr/bin/python3
"""Defines unit tests for Place views."""

import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from api.v1.app import app
from models import storage
from models.city import City
from models.place import Place


class TestPlacesView(unittest.TestCase):
    """Test cases for places view."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Reset storage."""
        storage.delete_all()
        storage.save()

    def test_get_places_by_city(self):
        """Test retrieving all Place objects of a City."""
        # Create a City and Place
        city = City(name="Test City")
        storage.new(city)
        storage.save()
        place = Place(name="Test Place", city_id=city.id)
        storage.new(place)
        storage.save()

        # Send GET request to /api/v1/cities/<city_id>/places
        response = self.app.get(f'/api/v1/cities/{city.id}/places')

        # Check response status code and content
        self.assertEqual(response.status_code, 200)
        places_data = response.get_json()
        self.assertEqual(len(places_data), 1)
        self.assertEqual(places_data[0]['name'], "Test Place")

    # Add more test cases for other endpoints...

if __name__ == '__main__':
    unittest.main()
