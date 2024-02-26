#!/usr/bin/python3
"""
Defines unit tests for User views.
"""

import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from api.v1.app import app
from models import storage
from models.user import User


class TestUsersView(unittest.TestCase):
    """Test cases for users view."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Reset storage."""
        storage.delete_all()
        storage.save()

    def test_get_users(self):
        """Test retrieving all User objects."""
        # Create users
        user1 = User(email="user1@example.com", password="password1")
        user2 = User(email="user2@example.com", password="password2")
        storage.new(user1)
        storage.new(user2)
        storage.save()

        # Send GET request to /api/v1/users
        response = self.app.get('/api/v1/users')

        # Check response status code and content
        self.assertEqual(response.status_code, 200)
        users_data = response.get_json()
        self.assertEqual(len(users_data), 2)

    @patch('api.v1.views.users.storage.get')
    def test_get_user(self, mock_get):
        """Test retrieving a specific User object."""
        # Create a User
        user = User(email="test@example.com", password="password")
        mock_get.return_value = user

        # Send GET request to /api/v1/users/<user_id>
        response = self.app.get('/api/v1/users/123')

        # Check response status code and content
        self.assertEqual(response.status_code, 200)
        user_data = response.get_json()
        self.assertEqual(user_data['email'], "test@example.com")

    @patch('api.v1.views.users.storage.get')
    def test_get_user_not_found(self, mock_get):
        """Test retrieving a non-existent User object."""
        mock_get.return_value = None

        # Send GET request to /api/v1/users/<user_id>
        response = self.app.get('/api/v1/users/123')

        # Check response status code and content
        self.assertEqual(response.status_code, 404)

    # Add similar test cases for other endpoints...

if __name__ == '__main__':
    unittest.main()
