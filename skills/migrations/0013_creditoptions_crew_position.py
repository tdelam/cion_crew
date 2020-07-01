# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0012_auto_20141008_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditoptions',
            name='crew_position',
            field=models.ForeignKey(blank=True, to='skills.CrewPosition', null=True),
            preserve_default=True,
        ),
    ]
