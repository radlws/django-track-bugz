# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_bugz', '0004_auto_20141224_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('attachment', models.FileField(help_text=b'(optional)', upload_to=b'attachments/')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('user', models.CharField(max_length=255, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterField(
            model_name='milestone',
            name='end_date_actual',
            field=models.DateField(null=True, verbose_name='Actual End Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='milestone',
            name='end_date_scheduled',
            field=models.DateField(null=True, verbose_name='Scheduled End Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='milestone',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Start Date', blank=True),
            preserve_default=True,
        ),
    ]
