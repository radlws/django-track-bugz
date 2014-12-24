# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_bugz', '0002_remove_milestone_end_date_actual'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='end_date_actual',
            field=models.DateTimeField(default=None, verbose_name='Actual End Date'),
            preserve_default=False,
        ),
    ]
