# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_auto_20140930_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name_plural': 'Skills'},
        ),
        migrations.RemoveField(
            model_name='skills',
            name='affiliations',
        ),
    ]
