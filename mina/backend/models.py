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
import uuid
#from git import GitCommandError


class UserProfile(models.Model):
    user = models.ForeinKey('auth.User')
    uuid = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        editable=False)


class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.IntegerField()
    body = models.CharField(max_length=200000)
    uuid = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
        editable=False)


@receiver(post_save, sender=User)
def auto_create_repo(instance, **kwargs):
    try:
        repoPath = 'repos/' + uuid.uuid4().hex
        ## create user profile
        ## link ^^^ to user
        EG.init_repo(repoPath, bare=False)
        push_to_git(repoPath,
            index_prefix=settings.ELASTIC_GIT_INDEX_PREFIX,
            es_host=settings.ELASTICSEARCH_HOST)
    except ValueError:
        raise
        worksapce.refresh_index()

#posting to EG
@receiver(post_save, sender=Story)
def auto_save_to_git(instance, **kwargs):
    

    data = TestStory({
        "title": instance.title,
        "author": instance.author,
        "category": instance.category,
        "body": instance.body,
        "uuid":uuid.uuid4().hex}
        )

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




