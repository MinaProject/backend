from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stories, name='stories'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^create_story/', views.create_story, name='create_Story'),
    url(r'^delete_story/', views.delete_story, name='delete_story'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^view_user/', views.view_user, name='view_user'),
    url(r'^view_user_stories/', views.view_user_stories,
        name='view_user_stories'),
    url(r'^view_categogry_stories/', views.view_category_stories,
        name='view_categogry_stories'),
    url(r'^update_version_correct/', views.update_version_correct,
        name='update_version_correct'),
    url(r'^update_story/', views.update_story, name='update_story'),
    url(r'^story', views.view_story, name='view_story')
]
