from django.shortcuts import render
from django.http import HttpResponse

from backend.utils import pull_from_git
from django.http import JsonResponse
import json
import uuid
from django.contrib.auth.models import User, UserManager

def stories(request):
    listOfStories =  pull_from_git('repos/test_content',
            index_prefix='',
            es_host='http://localhost:9200')
    return HttpResponse(listOfStories)

def create_user(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            name=data['name']
            username=data['username']
            uuid=uuid.uuid4().hex

            user = User.objects.create_user(username, email=None)
            ##### create git repo for that user
            return HttpResponse('created user')
        except:
            print 'nope'
    return HttpResponse('never created user')

