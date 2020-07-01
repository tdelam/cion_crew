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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=40)),
                ('province', models.IntegerField(default=0, choices=[(0, b'Province/Territory'), (1, b'Alberta'), (2, b'British Columbia'), (3, b'Manitoba'), (4, b'New Brunswick'), (5, b'Newfoundland & Labraador'), (6, b'Northwest Territories'), (7, b'Nova Scotia'), (8, b'Nunavut'), (9, b'Ontario'), (10, b'Prince Edward Island'), (11, b'Quebec'), (12, b'Saskatchewan'), (13, b'Yukon')])),
                ('postal_code', models.CharField(max_length=7)),
                ('phone', models.CharField(max_length=40)),
                ('website', models.URLField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
