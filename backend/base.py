from django.test import TestCase
from backend import utils


class BaseTestCase(TestCase):

    def mk_workspace(self):
        ws = utils.setup_workspace('repos/test_content',
                                   '',
                                   'http://localhost:9200')
        return ws
