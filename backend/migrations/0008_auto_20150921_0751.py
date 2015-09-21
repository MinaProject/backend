# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20150917_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='timestamp',
            new_name='update_count',
        ),
    ]
