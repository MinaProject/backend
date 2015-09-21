from django.http import HttpResponse
from backend.utils import pull_from_git, delete_from_git
import json
from django.contrib.auth.models import User
from models import Story, UserProfile
import uuid


def stories(request):
    listOfStories = pull_from_git('repos/test_content',
                                  index_prefix='',
                                  es_host='http://localhost:9200', uuid=None,
                                  category=None)
    return HttpResponse(listOfStories)


def view_story(request):
    if request.method == 'POST':
        try:
            uuid = request.POST
            story = Story.objects.get(uuid=uuid)
            response = HttpResponse()
            response.body = {"title": story.title,
                             "author": story.author,
                             "category": story.category,
                             "body": story.body}
            return response
        except:
            print ''
    response = HttpResponse()
    response.body = 'story not found'
    return response


def view_user_stories(request):
    if request.method == 'POST':
        try:
            uuid = request.POST
            stories = pull_from_git('repos/test_content',
                                    index_prefix='',
                                    es_host='http://localhost:9200',
                                    uuid=uuid,
                                    category=None)
            return HttpResponse(stories)
        except:
            print ''
    return HttpResponse('story not found')


def view_category_stories(request):
    if request.method == 'POST':
        try:
            category = request.POST
            stories = pull_from_git('repos/test_content',
                                    index_prefix='',
                                    es_host='http://localhost:9200',
                                    uuid=None,
                                    category=category)
            return HttpResponse(stories)
        except:
            print ''
    return HttpResponse('story not found')


def create_user(request):
    if request.method == 'POST':
        try:
            data = request.POST
            user = User.objects.create_user(username=data['username'],
                                            email=None,
                                            first_name=data['name'],
                                            last_name=data['surname'],
                                            password=data['password'])
            UserProfile.objects.create(user=user, uuid=uuid.uuid4().hex)

            response = HttpResponse()
            response.body = 'created'
            return response
        except:
            print ''
    response = HttpResponse()
    response.body = 'not created'
    return response


def create_story(request):
    if request.method == 'POST':
        try:
            data = request.POST
            Story.objects.create(title=data['title'],
                                 author=data['author'],
                                 category=data['category'],
                                 body=data['body'],
                                 uuid=uuid.uuid4().hex)
            response = HttpResponse()
            response.body = 'created'
            return response
        except:
            print ''
    response = HttpResponse()
    response.body = 'not created'
    return response


def delete_story(request):
    if request.method == 'POST':
        try:
            data = request.POST
            storyUUID = data['uuid']
            delete_from_git(storyUUID)
            response = HttpResponse()
            response.body = 'deleted'
            return response
        except:
            print ''
    response = HttpResponse()
    response.body = 'not deleted'
    return response


def delete_user(request):
    if request.method == 'POST':
        try:
            data = request.POST
            userUsername = data['username']
            deleteUser = User.objects.get(username=userUsername)
            deleteUser.delete()
            response = HttpResponse()
            response.body = 'deleted'
            return response
        except:
            print 'codie'
    response = HttpResponse()
    response.body = 'not deleted'
    return response


def view_user(request):
    if request.method == 'POST':
        try:
            uuid = request.POST
            user = UserProfile.objects.get(uuid=uuid).user
            return HttpResponse(json.dumps([dict(user.to_object())]))
        except:
            print ''
    return HttpResponse('user not found')
