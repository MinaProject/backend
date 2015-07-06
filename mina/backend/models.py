import os

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models import F
from django.db.models.signals import (
    post_save, post_delete, m2m_changed)
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from elasticgit import EG
from elasticgit.models import Model, IntegerField, TextField
from elasticinit import TestStory
from backend.utils import push_to_git
#from git import GitCommandError

class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.IntegerField()
    body = models.CharField(max_length=200000)

class User(models.Model):
    UUID = models.IntegerField()
    surname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

#posting to EG
@receiver(post_save, sender=Story)
def auto_save_to_git(instance, **kwargs):
    

    data = TestStory({
        "title": instance.title,
        "author": instance.author,
        "category": instance.category,
        "body": instance.body})

    try:
        workspace = EG.workspace(settings.GIT_REPO_PATH,
            index_prefix=settings.ELASTIC_GIT_INDEX_PREFIX,
            es={'urls': [settings.ELASTICSEARCH_HOST]})
        workspace.setup('Codie Roelf', 'codiebeulaine@gmail.com')
        workspace.save(data, 'saving')
        workspace.refresh_index()
        push_to_git(settings.GIT_REPO_PATH,
            index_prefix=settings.ELASTIC_GIT_INDEX_PREFIX,
            es_host=settings.ELASTICSEARCH_HOST)
    except ValueError:
        raise
        workspace.refresh_index()




