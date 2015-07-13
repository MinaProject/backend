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
	data = {
        "title": 'Story Title',
        "author": 'The Author',
        "category": '1',
        "body": 'The Story'}

	
Contents:

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

