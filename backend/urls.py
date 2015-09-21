from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stories, name='stories'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^create_story/', views.create_story, name='create_Story'),
    url(r'^delete_story/', views.delete_story, name='delete_story'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^view_user_info/', views.view_user, name='view_user_info'),
    url(r'^story', views.view_story, name='view_story')
]
