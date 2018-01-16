from django.test import TestCase

# Create your tests here.
from .views import *
from .workers import *

class numberInputTests(TestCase):
    """Unit testing for components in views and workers"""
    
    def test_cleanAndCheckNumber_strings_will_not_pass(self):
        """cleanAndCheckNumber() raises an error when string input is
        alphanumerical."""
        self.assertRaises(ValueError, cleanAndCheckNumber, 'text')

    def test_cleanAndCheckNumber_out_of_range(self):
        """cleanAndCheckNumber() raises an error if numeric input value is
        out of desired range."""
        self.assertRaises(ValueError, cleanAndCheckNumber, "0")
        self.assertRaises(ValueError, cleanAndCheckNumber, "101")
        self.assertEquals(cleanAndCheckNumber("50"), 50)
