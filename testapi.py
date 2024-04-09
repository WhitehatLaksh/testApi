import unittest
import requests

class TestYourAPI(unittest.TestCase):
    base_url = "http://your-api-url.com"

    def test_get_request(self):
        response = requests.get(self.base_url + "/endpoint")
        self.assertEqual(response.status_code, 200)
        self.assertIn("expected_response_data", response.json())

    def test_post_request(self):
        payload = {"key": "value"}
        response = requests.post(self.base_url + "/endpoint", json=payload)
        self.assertEqual(response.status_code, 201)  # Assuming creation is successful
        # Additional assertions as needed

    def test_put_request(self):
        payload = {"key": "updated_value"}
        response = requests.put(self.base_url + "/endpoint/1", json=payload)
        self.assertEqual(response.status_code, 200)
        # Additional assertions as needed

    def test_delete_request(self):
        response = requests.delete(self.base_url + "/endpoint/1")
        self.assertEqual(response.status_code, 204)  # Assuming successful deletion
        # Additional assertions as needed

if __name__ == "__main__":
    unittest.main()
