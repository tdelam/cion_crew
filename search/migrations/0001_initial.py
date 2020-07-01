# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q', models.CharField(max_length=50)),
                ('search_date', models.DateTimeField(default=datetime.datetime.now)),
                ('ip_address', models.IPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
