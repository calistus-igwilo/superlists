from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    """ A deliberately failing test"""
    
    def test_bad_maths(self):
        """ A silly failing test"""
        self.assertEqual(1 + 1, 3)

