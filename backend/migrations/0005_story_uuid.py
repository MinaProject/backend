# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_story_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='uuid',
            field=models.CharField(null=True, editable=False, max_length=32, blank=True, unique=True, db_index=True),
        ),
    ]
