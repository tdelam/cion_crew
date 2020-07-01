# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0008_skills_affiliations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='affiliations',
            field=models.IntegerField(default=0, choices=[(0, b'Affiliations'), (1, b'DGC Directors Guild of Canada'), (2, b'IATSE'), (3, b'ACTRA - Alliance of Cinema, Television and Radio Artists'), (4, b'WGC Writers Guild of Canada ')]),
        ),
    ]
