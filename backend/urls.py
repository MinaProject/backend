from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stories, name='stories'),
    url(r'^createUser/', views.create_user, name='create_user'),
    url(r'^createStory/', views.create_story, name='create_Story'),
    url(r'^deleteStory/', views.delete_story, name='delete_story'),
    url(r'^viewUserStory', views.view_user_stories, name='user stories')
]
