# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0017_remove_creditoptions_weeks_worked'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='resident',
            field=models.BooleanField(default=False, verbose_name=b'I am a Northern Ontario resident'),
            preserve_default=True,
        ),
    ]
