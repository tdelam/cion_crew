# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0022_skills_available_as'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='available_as',
            field=models.TextField(null=True, blank=True),
        ),
    ]
