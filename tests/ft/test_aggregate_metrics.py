import os
from urllib import response

import requests
from unittest import TestCase

class TestAggregateMetrics(TestCase):
    BASE_URL = "http://localhost:8000"
    DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "challenge_data")

    def test_root_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_aggregate_metrics_endpoint(self):
        # I WANT TO HAVE BETTER TESTING BUT THIS IS GOOD ENOUGH FOR NOW

        # This is the test file provided
        test_file_path = os.path.join(self.DATA_DIR, "example_station_data.csv")

        with open(test_file_path, "rb") as f:
            response = requests.post(f"{self.BASE_URL}/aggregate-metrics", files={"file": f})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['QDR1']['healthy'])
        self.assertTrue(response.json()['QDR2']['healthy'])
        self.assertTrue(response.json()['QDR3']['healthy'])
        self.assertTrue(response.json()['QDR4']['healthy'])
        self.assertTrue(response.json()['QDR5']['healthy'])
        self.assertTrue(response.json()['QDR6']['healthy'])
        self.assertFalse(response.json()['QDR7']['healthy'])

    def test_fail_to_aggregate_metrics(self):
        # This is the test file provided
        test_file_path = os.path.join(self.DATA_DIR, "bad_data.txt")

        with open(test_file_path, "rb") as f:
            response = requests.post(f"{self.BASE_URL}/aggregate-metrics", files={"file": f})
        self.assertEqual(response.status_code, 400)
