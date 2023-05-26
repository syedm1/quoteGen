import unittest
from unittest.mock import patch
from flask import Flask
from flask.testing import FlaskClient
from main import app
import json


class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_diagnostic_route(self):
        response = self.app.get('/diagnostic')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'ok')

    def test_get_quote_route(self):
        response = self.app.get('/api/quote')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', data)
    
    def test_get_random_quote_route(self):
        response = self.app.get('/api/random')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', data)

    def test_invalid_route(self):
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)
 


if __name__ == '__main__':
    unittest.main()