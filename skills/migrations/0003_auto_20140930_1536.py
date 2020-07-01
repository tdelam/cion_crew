# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20140930_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditoptions',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]
