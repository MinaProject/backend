from django.contrib.auth.models import User
from backend.base import BaseTestCase
from django.test.client import Client


class TestModels(BaseTestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            'testuser', 'test@gmail.com', password='test')
        self.client = Client()
        self.client.login(username='testuser', password='test')

        self.workspace = self.mk_workspace()

    def test_user_info(self):
        user = User.objects.create_user('foo', 'foo@example.org', 'bar')
        user.first_name = 'Foo'
        user.last_name = 'Bar'
        user.save()

        self.assertEqual(
            ('Foo', 'foo@example.org'),
            (user.first_name, user.email))
