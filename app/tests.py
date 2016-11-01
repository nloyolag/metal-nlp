import unittest
from urlparse import urlparse
import os
import app
import views

##################################################################
# Test Suite Name: TestSubmitView
# Explanation: Test suite that tests the submit view
#
# Included tests:
#   - GET: Test if the view renders correctly
#   - POST: Test the error message when submitting the form
#           icnorrectly
#   - POST: Test a correct form submission
##################################################################

class TestSubmitView(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.app.test_client()

    def test_view_render(self):
        response = self.app.get('/')
        self.assertTrue('lyrics' in response.data)
        self.assertEquals(response.status_code, 200)

    def test_view_error(self):
        response = self.app.post(
            '/',
            content_type='multipart/form-data',
            data={
                'lyrics': ''
            }
        )
        self.assertTrue('Please submit lyrics from a metal song' in response.data)

    def test_form_submission(self):
        pass
        # response = self.app.post(
        #     '/',
        #     content_type='multipart/form-data',
        #     data={
        #         'lyrics': 'Satan is glorious.'
        #     },
        #     follow_redirects=False
        # )
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(urlparse(response.location).path, '/evaluation')

##################################################################
# Test Suite Name: TestEvaluationView
# Explanation: Test suite that tests the evaluation view
#
# Included tests:
#   - GET: Test if the view renders correctly
#   - POST: Test the error message if the form is incomplete
#   - POST: Test a correct form submission
##################################################################

class TestEvaluationView(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.app.test_client()
        with self.app.session_transaction() as sess:
            sess['cluster_info'] = {
                'new_data': {
                    'topic_label': 'Gore',
                    'genre_label': 'Death Metal',
                    'frequent_words': 'guts blood',
                    'lyrics': ['yeah', 'killing']
                },
                2018: {
                    'album': 'Human',
                    'artist': 'death',
                    'title': 'Flattening of Emotions',
                    'year': 1991,
                    'lyrics': ['Where is the person that could have been']
                }
            }

    def test_view_render(self):
        response = self.app.get('/evaluation')
        self.assertTrue('email' in response.data)
        self.assertTrue('Album' in response.data)
        self.assertTrue('Artist' in response.data)
        self.assertEquals(response.status_code, 200)

    def test_view_error(self):
        response = self.app.post(
            '/evaluation',
            content_type='multipart/form-data',
            data={
                'email': '',
                'evaluation1': None,
                'evaluation2': None,
                'evaluation3': None,
                'evaluation4': None,
                'evaluation5': None
            }
        )
        self.assertTrue('Please provide your email' in response.data)
        self.assertTrue('Please evaluate the recommendation' in response.data)

    def test_form_submission(self):
        response = self.app.post(
            '/evaluation',
            content_type='multipart/form-data',
            data={
                'email': 'chuck_schuldinner@gmail.com',
                'evaluation1': True,
                'evaluation2': True,
                'evaluation3': True,
                'evaluation4': True,
                'evaluation5': True
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, '/thanks')

##################################################################
# Test Suite Name: TestThanksView
# Explanation: Test suite that tests the thanks view
#
# Included tests:
#   - GET: Test if the view renders correctly
##################################################################

class TestThanksView(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.app.test_client()

    def test_view_render(self):
        response = self.app.get('/thanks')
        self.assertTrue('Thanks for submitting your response!' in response.data)
        self.assertEquals(response.status_code, 200)
