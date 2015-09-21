import os
from django.conf import settings
from django.db import models
from django.db.models.signals import (
    post_save)
from django.dispatch import receiver
from elasticgit import EG
from elasticinit import TestStory

join = os.path.join


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User')
    uuid = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        editable=False)


class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        editable=False)
    category = models.IntegerField()
    body = models.CharField(max_length=200000)
    uuid = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
        editable=False)
    update_count = models.IntegerField(default=0)
    co_authors = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
        editable=False)


# @receiver(post_init, sender=User)
# def auto_create_profile(instance, **kwargs):
#     try:
#         #userUUID = uuid.uuid4().hex
#         # # creating repo on GitHub
#         # gh = GitHub('minaglobalfoundation@gmail.com',
#         #             password='minafoundation15')
#         # githubRepo = gh.create_repo(userUUID, description=u'',
#         #                             homepage=u'',
#         #                             private=False,
#         #                             has_issues=True,
#         #                             has_wiki=True,
#         #                             auto_init=True,
#         #                             gitignore_template=u'')
#         # githubRepo.create_blob('hello', 'utf-8')
#         # githubRepo.create_commit('first commit', '', '')

#         # # creating local repo
#         # repoPath = 'repos/' + userUUID
#         #UserProfile.objects.create(user=instance, uuid=userUUID)
#         # EG.init_repo(repoPath, bare=False)

#         # # creating workspace in local repo
#         # workspace = EG.workspace(repoPath,
#         #                          index_prefix='',
#         #                          es={'urls': ['http://localhost:9200']})

#         # # pushing local repo to GitHub repo
#         # workspace.repo.create_remote('origin', githubRepo.html_url)
#         # repo = workspace.repo
#         # remote = repo.remote()
#         # remote.fetch()
#         # remote_master = remote.refs.master
#         # remote.push(remote_master.remote_head)
#         print('nothing')
#     except ValueError:
#         print''


# posting to EG
@receiver(post_save, sender=Story)
def auto_save_to_git(instance, **kwargs):
    data = TestStory({
        "title": instance.title,
        "author": instance.author,
        "category": instance.category,
        "body": instance.body,
        "uuid": instance.uuid,
        "update_count": instance.update_count,
        "co_authors": instance.co_authors})

    try:
        # EG.init_repo('repos/test_content', bare=False)
        ws = EG.workspace(settings.GIT_REPO_PATH,
                          index_prefix=None,
                          es={'urls': ['http://localhost:9200']})
        ws.setup('Codie Roelf', 'codiebeulaine@gmail.com')
        ws.save(data, 'saving')
        if ws.repo.remotes:
            repo = ws.repo
            remote = repo.remote()
            remote.fetch()
            remote_master = remote.refs.master
            remote.push(remote_master.remote_head)
        ws.refresh_index()

    except ValueError:
        print "error"
