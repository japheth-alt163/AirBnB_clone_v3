#!/usr/bin/python3
"""Defines unit tests for Amenity views."""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from flask import Flask, jsonify
from api.v1.app import app
from models import storage
from models.amenity import Amenity


class TestAmenitiesView(unittest.TestCase):
    """Test cases for amenities view."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Reset storage."""
        storage.delete_all()
        storage.save()

    def test_get_amenities(self):
        """Test retrieving all Amenity objects."""
        # Create amenities
        amenity1 = Amenity(name="Amenity1")
        amenity2 = Amenity(name="Amenity2")
        storage.new(amenity1)
        storage.new(amenity2)
        storage.save()

        # Send GET request to /api/v1/amenities
        response = self.app.get('/api/v1/amenities')

        # Check response status code and content
        self.assertEqual(response.status_code, 200)
        amenities_data = response.get_json()
        self.assertEqual(len(amenities_data), 2)

    @patch('api.v1.views.amenities.storage.get')
    def test_get_amenity(self, mock_get):
        """Test retrieving a specific Amenity object."""
        # Create an Amenity
        amenity = Amenity(name="Test Amenity")
        mock_get.return_value = amenity

        # Send GET request to /api/v1/amenities/<amenity_id>
        response = self.app.get('/api/v1/amenities/123')

        # Check response status code and content
        self.assertEqual(response.status_code, 200)
        amenity_data = response.get_json()
        self.assertEqual(amenity_data['name'], "Test Amenity")

    @patch('api.v1.views.amenities.storage.get')
    def test_get_amenity_not_found(self, mock_get):
        """Test retrieving a non-existent Amenity object."""
        mock_get.return_value = None

        # Send GET request to /api/v1/amenities/<amenity_id>
        response = self.app.get('/api/v1/amenities/123')

        # Check response status code and content
        self.assertEqual(response.status_code, 404)

    # Add similar test cases for other endpoints...

if __name__ == '__main__':
    unittest.main()
