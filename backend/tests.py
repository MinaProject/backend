from mock import patch
from views import create_user, create_story
from django.http import HttpRequest
import unittest
from django.contrib.auth.models import User
from models import Story


class TestModels(unittest.TestCase):

    def test_user_create(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {"name": 'foo',
                        "surname": 'bar',
                        "username": 'foobar',
                        "password": 'foobar'}
        with patch.object(User.objects, 'create_user'):
            assert create_user(request).body == 'created'

    def test_story_create(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {"title": 'foo',
                        "author": 'bar',
                        "category": 1,
                        "body": 'foobar'}
        with patch.object(Story.objects, 'create'):
            assert create_story(request).body == 'created'
