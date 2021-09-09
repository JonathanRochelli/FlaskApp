import unittest

from app import app

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_something(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_other(self):
        response = self.app.get('/goodbye', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
