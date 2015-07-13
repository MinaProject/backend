from django.shortcuts import render
from django.http import HttpResponse
from .models import Story
from backend.utils import pull_from_git
from django.http import JsonResponse
import json

def stories(request):
	listOfStories =  pull_from_git('repos/test_content',
            index_prefix='',
            es_host='http://localhost:9200')
	return HttpResponse(listOfStories)