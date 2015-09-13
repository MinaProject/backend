from django.http import HttpResponse
from backend.utils import pull_from_git
import json
from django.contrib.auth.models import User
from models import Story


def stories(request):
    listOfStories = pull_from_git('repos/test_content',
                                  index_prefix='',
                                  es_host='http://localhost:9200')
    return HttpResponse(listOfStories)


def create_user(request):
    print(request.method)
    if request.method == 'POST':
        try:
            print(request.POST)
            data = request.POST
            print(data)
            User.objects.create_user(username=data['username'],
                                     email=None,
                                     first_name=data['name'],
                                     last_name=data['surname'],
                                     password=data['password'])
            response = HttpResponse()
            response.body = 'created'
            return response
        except:
            print 'nope'
    response = HttpResponse()
    response.body = 'not created'
    return response


def create_story(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Story.create(title=data['title'],
                         author=data['author'],
                         category=data['category'],
                         body=data['body'])
            return HttpResponse.__init__(content='',
                                         content_type=None,
                                         status=201,
                                         reason='Story successfully created')
        except:
            print 'nope'
    return HttpResponse.__init__(content='',
                                 content_type=None,
                                 status=400,
                                 reason='Story not created')


def view_user_stories(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            userUUID = data['uuid']
            listOfStories = pull_from_git('repos/' + userUUID,
                                          index_prefix='',
                                          es_host='http://localhost:9200')
            return HttpResponse(listOfStories)
        except:
            print 'nope'
    return HttpResponse('Never found user')
