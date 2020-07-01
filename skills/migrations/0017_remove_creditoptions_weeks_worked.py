# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0016_creditoptions_weeks_worked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditoptions',
            name='weeks_worked',
        ),
    ]
