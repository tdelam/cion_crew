# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0013_creditoptions_crew_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditoptions',
            name='credit',
            field=models.ForeignKey(blank=True, to='skills.Credit', null=True),
        ),
    ]
