# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20150714_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='co_authors',
            field=models.CharField(null=True, editable=False, max_length=32, blank=True, unique=True, db_index=True),
        ),
        migrations.AddField(
            model_name='story',
            name='timestamp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.CharField(unique=True, max_length=32, editable=False, db_index=True),
        ),
    ]
