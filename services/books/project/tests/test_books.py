# services/books/project/tests/test_users.py


import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_books(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/books/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success books', data['status'])


if __name__ == '__main__':
    unittest.main()
