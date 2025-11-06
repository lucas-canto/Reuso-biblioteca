import unittest
from unittest.mock import patch, MagicMock
from http_module import get_data
import requests

class TestHttpModule(unittest.TestCase):

    @patch('http_module.requests.get')
    def test_get_data_success(self, mock_get):
        """
        Test get_data function for a successful request.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        url = "http://fakeurl.com"
        data = get_data(url)

        self.assertEqual(data, {"key": "value"})
        mock_get.assert_called_once_with(url, timeout=5)
        mock_response.raise_for_status.assert_called_once()

    @patch('http_module.requests.get')
    def test_get_data_failure(self, mock_get):
        """
        Test get_data function for a failed request.
        """
        mock_get.side_effect = requests.exceptions.RequestException("Test error")

        url = "http://fakeurl.com"
        data = get_data(url)

        self.assertIsNone(data)
        mock_get.assert_called_once_with(url, timeout=5)

if __name__ == '__main__':
    unittest.main()
