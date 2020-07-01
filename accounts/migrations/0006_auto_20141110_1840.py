# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='private',
            field=models.BooleanField(default=False, verbose_name=b'Please make my address private.'),
        ),
    ]
