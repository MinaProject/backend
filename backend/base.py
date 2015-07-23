from django.test import TestCase
from backend import utils


class BaseBackendTestCase(TestCase):

    def mk_workspace(self):
        ws = utils.setup_workspace('repos/test_content',
                                   index_prefix='',
                                   es={'urls': ['http://localhost:9200']})
