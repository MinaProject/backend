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
            password=data['password']
            uuid=uuid.uuid4().hex

            user = User.objects.create_user(username, email=None)
            ##### create git repo for that user
            return HttpResponse('created user')
        except:
            print 'nope'
    return HttpResponse('never created user')

def view_user_stories(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            userUUID = data['uuid']
            url = data['url']
            listOfStories = pull_from_git('repos/' + uuid,
                index_prefix='',
                es_host='http://localhost:9200')
            return HttpResponse(listOfStories)
        except:
            print 'nope'
    return HttpResponse('Never found user')

def delete_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            userUUID = data['uuid']
            url = data['url']
            delete_from_git('repos/' + uuid,
                index_prefix='',
                es_host='http://localhost:9200')
            ## delete user here!!
            return HttpResponse('deleted user')
        except:
            print 'nope'
    return  HttpResponse('could not find user')

