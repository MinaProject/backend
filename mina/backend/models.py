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
def auto_save_to_git(sender, instance, created, **kwargs):
    

    data = TestStory({
        "title": instance.title,
        "author": instance.author,
        "category": instance.category,
        "body": instance.body})

    try:
        workspace = EG.workspace('/Users/codieroelf/repositories/backend/mina')
        workspace.setup('Codie Roelf', 'codiebeulaine@gmail.com')
        workspace.save(data, 'saving')
        workspace.refresh_index()
    except ValueError:
        workspace.refresh_index()




