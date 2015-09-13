from backend.base import BaseTestCase
from mock import patch
from views import create_user
import json
from django.http import HttpResponse
from django.http import HttpRequest
import unittest
import requests
from django.contrib.auth.models import User


class TestModels(unittest.TestCase):

    def test_user_info(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {"name": 'foo',
                        "surname": 'bar',
                        "username": 'foobar',
                        "password": 'foobar'}
        with patch.object(User.objects, 'create_user') as get_mock:
        	get_mock.return_value.body == 'not created'
        	assert create_user(request).body == 'created'
