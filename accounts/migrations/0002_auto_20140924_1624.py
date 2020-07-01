# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
