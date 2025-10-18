import requests
from unittest import TestCase


class TestAggregateMetrics(TestCase):
    BASE_URL = "http://localhost:8000"

    def test_root_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_aggregate_metrics_endpoint(self):
        # THIS IS JUST TO ENSURE ITS WORKING
        response = requests.post(f"{self.BASE_URL}/aggregate-metrics")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})
