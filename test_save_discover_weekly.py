import unittest
from flask import session
from spotifyWeekly import app

class SpotifyAPITest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_save_discover_weekly(self):
        with self.app as client:
            # Simulate the login route
            response = client.get('/')
            self.assertEqual(response.status_code, 302)  # Expect a redirect

            # Simulate the redirect route with authorization code
            with client.session_transaction() as sess:
                sess['token_info'] = {'access_token': 'test_access_token', 'refresh_token': 'test_refresh_token'}
            response = client.get('/redirect?code=test_code')
            self.assertEqual(response.status_code, 302)  # Expect a redirect

            # Simulate the saveDiscoverWeekly route
            response = client.get('/saveDiscoverWeekly')
            self.assertEqual(response.status_code, 200)  # Expect a success response
            self.assertEqual(response.data.decode(), 'YOU DID IT GUUURLL !!!!')  # Expect the success message

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
