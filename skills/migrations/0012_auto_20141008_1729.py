# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0011_auto_20141001_1509'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CrewPosition',
        ),
        migrations.AlterModelOptions(
            name='crewposition',
            options={},
        ),
        migrations.RenameField(
            model_name='credit',
            old_name='category',
            new_name='crew_position',
        ),
    ]
