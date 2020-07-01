# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0020_auto_20141015_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='cpma',
            field=models.BooleanField(default=False, verbose_name=b'CMPA Member'),
            preserve_default=True,
        ),
    ]
