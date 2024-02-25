#!/usr/bin/python3
"""Unit tests for the API endpoints defined in index.py."""

import unittest
from api.v1.views.index import app_views

class TestIndexViews(unittest.TestCase):
    """Test cases for the API endpoints defined in index.py."""

    def test_status_endpoint(self):
        """Test the /status endpoint."""
        tester = app_views.test_client(self)
        response = tester.get('/status')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
