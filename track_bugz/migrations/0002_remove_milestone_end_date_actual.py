# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_bugz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestone',
            name='end_date_actual',
        ),
    ]
