# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20141027_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
