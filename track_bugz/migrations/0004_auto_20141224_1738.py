# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_bugz', '0003_milestone_end_date_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='end_date_actual',
            field=models.DateTimeField(null=True, verbose_name='Actual End Date', blank=True),
            preserve_default=True,
        ),
    ]
