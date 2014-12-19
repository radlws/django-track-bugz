# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('attachment', models.FileField(help_text=b'(optional)', upload_to=b'attachments/')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version_tag', models.CharField(max_length=50, verbose_name='Name')),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date_scheduled', models.DateTimeField(verbose_name='Scheduled End Date')),
                ('end_date_actual', models.DateTimeField(verbose_name='Actual End Date')),
            ],
            options={
                'verbose_name': 'Milestone',
                'verbose_name_plural': 'Milestones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=250, verbose_name='Description', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Submited date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('status', models.CharField(default=b'A', max_length=1, verbose_name='Status', choices=[(b'A', 'Active'), (b'P', 'In progress'), (b'R', 'Resolved'), (b'C', 'Closed')])),
                ('priority', models.IntegerField(default=3, verbose_name='Priority', choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')])),
                ('ticket_type', models.CharField(default=b'B', max_length=1, verbose_name='Ticket type', choices=[(b'B', 'Bug'), (b'T', 'Task'), (b'F', 'Feature'), (b'E', 'Enhancement'), (b'I', 'Inquiry')])),
                ('assigned_to', models.ForeignKey(verbose_name='Assigned to', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('milestone', models.ForeignKey(verbose_name='Milestone', blank=True, to='track_bugz.Milestone', null=True)),
                ('opened_by', models.ForeignKey(related_name='opened_by', verbose_name='Opened By', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(verbose_name='Project', to='track_bugz.Project')),
            ],
            options={
                'ordering': ('priority', 'title'),
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='track_bugz.Project'),
            preserve_default=True,
        ),
    ]
