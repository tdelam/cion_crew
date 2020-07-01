# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_auto_20140930_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditoptions',
            name='year',
            field=models.IntegerField(help_text=b'e.g. 1995', max_length=4, null=True, blank=True),
        ),
    ]
