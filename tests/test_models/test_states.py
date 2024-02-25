#!/usr/bin/python3
"""Defines unit tests for views/states.py."""

import unittest
from unittest.mock import patch
from io import StringIO
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.state import State


class TestStatesView(unittest.TestCase):
    """Test cases for states view."""

    def setUp(self):
        """Set up test client."""
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.app.testing = True
        self.client = self.app.test_client()

    def test_get_states(self):
        """Test retrieving all State objects."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            response = self.client.get('/api/v1/states')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'State', response.data)
        self.assertTrue(fake_out.getvalue().startswith('SELECT'))

    def test_get_state(self):
        """Test retrieving a State object."""
        state = State(name="Test State")
        storage.new(state)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            response = self.client.get(f'/api/v1/states/{state.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test State', response.data)
        self.assertTrue(fake_out.getvalue().startswith('SELECT'))


if __name__ == '__main__':
    unittest.main()
