import mock
from mock import patch
from views import (create_user, create_story, delete_user, delete_story,
                   view_story, view_user_stories, stories,
                   view_category_stories, view_user)
from django.http import HttpRequest
import unittest
from models import Story, UserProfile
from django.contrib.auth.models import User
import elasticgit


class TestCRUD(unittest.TestCase):

    @mock.patch('django.db.models.signals.post_save', autospec=True)
    def test_story_user(self, mock_post_save):

        # test create user
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {"name": 'test',
                        "surname": 'surnameTest',
                        "username": 'tester',
                        "password": 'tester'}
        assert create_user(request).body == 'created'

        # test create story
        user = User.objects.get(username='tester')
        userProfile = UserProfile.objects.get(user=user)
        uuid = userProfile.uuid
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {"title": 'foo',
                        "author": uuid,
                        "category": 1,
                        "body": 'foobar',
                        "update_count": 0,
                        "co_authors": None}
        assert create_story(request).body == 'created'

        # test view all stories
        with patch.object(elasticgit.workspace.Workspace, 'pull'):
            assert stories(request) != []

        # test view specific story
        story = Story.objects.get(author=uuid)
        storyUUID = story.uuid
        request = HttpRequest()
        request.method = 'POST'
        request.POST = storyUUID
        with patch.object(elasticgit.workspace.Workspace, 'pull'):
            assert view_story(request).body != 'story not found'

        # test view all category stories
        request.POST = story.category
        with patch.object(elasticgit.workspace.Workspace, 'pull'):
            assert view_category_stories(request) != 'story not found'

        # test view all user stories
        request.POST = story.uuid
        with patch.object(elasticgit.workspace.Workspace, 'pull'):
            assert view_user_stories(request) != 'story not found'

        # test view user information
        request.POST = uuid
        assert view_user(request) != 'user not found'

        # test delete story
        story = Story.objects.get(title='foo', body='foobar')
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {"uuid": story.uuid}
        assert delete_story(request).body == 'deleted'

        # test delete user
        request2 = HttpRequest()
        request2.method = 'POST'
        request2.POST = {"username": 'tester'}
        assert delete_user(request2).body == 'deleted'
