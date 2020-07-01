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
            name='SkillsAffiliations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('imdb', models.URLField(null=True, blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('affiliations', models.IntegerField(default=0, choices=[(0, b'Affiliations'), (1, b'DGC Directors Guild of Canada'), (2, b'IATSE'), (3, b'ACTRA - Alliance of Cinema, Television and Radio Artists'), (4, b'WGC Writers Guild of Canada ')])),
                ('other', models.CharField(max_length=150, null=True, blank=True)),
                ('local_number', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
