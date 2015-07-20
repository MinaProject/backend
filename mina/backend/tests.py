from django.test import TestCase
from backend.models import Story
from backend.models import diffUser
import uuid
from django.test import Client
# Create your tests here.

class StoryTestCase(TestCase):

	def test_stories_response_code(self):
		c = Client()
		response = c.get('/backend/')
		self.assertEqual(response.status_code, 200)