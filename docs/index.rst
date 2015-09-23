.. Mina documentation master file, created by
   sphinx-quickstart on Mon Jul 13 21:03:04 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Mina's documentation!
================================

Mina is currently a UCT Computer Science Honours' project in conjunction with Praekelt Foundation. The aim of this project is to provide
an open-source tool for the collaborative or singular authoring and viewing of textual content around the topics of sex, love, relationships and HIV/AIDS. These docs have been written specifically for the backend of the project.

User Model
----------

The User Model is a JSON object that is received by the backend via Django. The model is as follows:

.. code:: python

  User = {"Name":'foo',
  "Surname":'bar',
  "Username":'foobar',
  "Password": 'foobar93'}

Story Model
-----------

The Story model is a JSON object that is received by the backend via Django and passed straight into an elasticgit model. The model is as follows:

.. code:: python

  Story = {"title": 'Story Title',
        "author": 'Author UUID',
        "category": '1',
        "body": 'The Story',
        "update_count": 'Integer, defaults to 0',
        "co_authors": 'UUID of co_author'}


URLs
----

At the moment this project is hosted locally and not on a server. Nonetheless the urls are as follows:

To create a user: backend/create_user
  This takes in an HttpRequest that has a POST method where the post contains json user model defined above
To create a story: backend/create_story
  This takes in an HttpRequest that has a POST method where the post contains json story model defined above
To delete a user: backend/delete_user
  This takes in an HttpRequest that has a POST method where the post contains uuid of the user to be deleted
To delete a story: backend/delete_story
  This takes in an HttpRequest that has a POST method where the post contains the uuid of the story to be     deleted
To view a user's info: backend/view_user
  This takes in an HttpRequest that has a POST method where the post contains uuid of the user to be viewed
To view all stories: backend/
  This takes any request as an argument and returs a list of all the stories
To view all user stories: backend/view_user_stories
  This takes a user uuid and returns a list of all the stories that user has created
To view all cetegory stories: backend/view_category_stories
  This takes in a category (integer), and returns all the stories in that category
To check if the user has the correct current story: backend/update_version_correct
  This takes in the stories update count as 'update_count' and the story's uuid as 'uuid', and returns 'story
  is up to date' if the story version is correct, else it returns the correct version of the story as "title",  "author", "category" and "body"
To update a story: backend/update_story
  This takes in the second user's uuid as "userUUID", the story permissions to change as "permissions" (either  'yes' or 'no', the story UUID as "uuid" and the changes as "changes". It returns 'updated' if the update was
  successfull and 'not updated if the update was not successfull.

.. toctree::
   :maxdepth: 2

