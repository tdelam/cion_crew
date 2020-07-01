# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0026_skills_cpma2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='cpma2',
        ),
    ]
