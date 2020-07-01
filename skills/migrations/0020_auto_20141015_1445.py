# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0019_auto_20141015_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditoptions',
            name='imdb_credited',
            field=models.BooleanField(default=False, verbose_name=b'IMDB Credited'),
        ),
    ]
