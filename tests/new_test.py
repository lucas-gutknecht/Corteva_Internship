import unittest
from flask import Flask, jsonify
from weather_app.weather_app import app

class FlaskApiTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup that runs once for the entire test case"""
        cls.app = app
        cls.client = app.test_client()

    def test_get_data(self):
        """Test the /get_data endpoint"""
        response = self.client.get('/get_data')
        
        self.assertEqual(response.status_code, 200)
        
        json_data = response.get_json()
        self.assertEqual(json_data["Results"][0]['date'], 19850101)

    
if __name__ == '__main__':
    unittest.main()
    