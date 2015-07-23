from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stories, name='stories'),
    url(r'^createUser/', views.create_user, name='user'),
    url(r'^viewUserStory', views.view_user_stories, name='user stories')
]
