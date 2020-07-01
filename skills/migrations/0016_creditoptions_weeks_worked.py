# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0015_auto_20141009_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditoptions',
            name='weeks_worked',
            field=models.IntegerField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
