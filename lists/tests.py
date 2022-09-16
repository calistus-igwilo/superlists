from django.test import TestCase
from django.urls import resolve
from lists.views import home_page 

# # Create your tests here.
# class SmokeTest(TestCase):
#     """ A deliberately failing test"""
    
#     def test_bad_maths(self):
#         """ A silly failing test"""
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

