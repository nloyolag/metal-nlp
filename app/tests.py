import unittest
from StringIO import StringIO
from urlparse import urlparse
import os
import app
from app import views

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
        pass

    def test_view_error(self):
        pass

    def test_form_submission(self):
        pass

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

    def test_view_render(self):
        pass

    def test_view_error(self):
        pass

    def test_form_submission(self):
        pass

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
        pass
