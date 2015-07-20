from django.conf.urls import include, url
from . import views
from django.contrib.auth.models import User, UserManager


urlpatterns = [
    url(r'^$', views.stories, name='stories'),
    url(r'^createUser/', views.create_user, name='user'),
    url(r'^viewUserStory', views.view_user_stories, name = 'user stories')
]
