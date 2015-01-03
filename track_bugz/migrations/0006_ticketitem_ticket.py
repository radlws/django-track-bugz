# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_bugz', '0005_auto_20150103_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketitem',
            name='ticket',
            field=models.ForeignKey(default=None, to='track_bugz.Ticket'),
            preserve_default=False,
        ),
    ]
