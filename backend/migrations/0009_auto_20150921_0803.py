# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20150921_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.CharField(max_length=32, editable=False, db_index=True),
        ),
    ]
