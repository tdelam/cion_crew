# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0025_auto_20141112_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='cpma2',
            field=models.BooleanField(default=False, verbose_name=b'CMPA Member'),
            preserve_default=True,
        ),
    ]
