from django.contrib.auth.models import User
from backend.base import BaseTestCase


class TestModels(BaseTestCase):

    def test_user_info(self):
        user = User.objects.create_user('foo', 'foo@example.org')
        user.first_name = 'Foo'
        user.last_name = 'Bar'

        self.assertEqual(
            ('Foo', 'foo@example.org'),
            (user.first_name, user.email))
