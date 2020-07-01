# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20141003_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='province',
            field=models.IntegerField(default=9, choices=[(0, b'Choose your province'), (1, b'Alberta'), (2, b'British Columbia'), (3, b'Manitoba'), (4, b'New Brunswick'), (5, b'Newfoundland & Labraador'), (6, b'Northwest Territories'), (7, b'Nova Scotia'), (8, b'Nunavut'), (9, b'Ontario'), (10, b'Prince Edward Island'), (11, b'Quebec'), (12, b'Saskatchewan'), (13, b'Yukon')]),
        ),
    ]
