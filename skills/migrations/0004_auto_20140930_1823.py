# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20140930_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='local_number',
        ),
        migrations.AlterField(
            model_name='creditoptions',
            name='year',
            field=models.IntegerField(help_text=b'e.g. 1995', max_length=4),
        ),
        migrations.AlterField(
            model_name='skills',
            name='affiliations',
            field=models.IntegerField(default=0, verbose_name=b'Union/Guilde Affiliation(s)', choices=[(0, b'Affiliations'), (1, b'DGC Directors Guild of Canada'), (2, b'IATSE'), (3, b'ACTRA - Alliance of Cinema, Television and Radio Artists'), (4, b'WGC Writers Guild of Canada ')]),
        ),
        migrations.AlterField(
            model_name='skills',
            name='other',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Other', blank=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='resume',
            field=models.FileField(upload_to=b'uploads/', null=True, verbose_name=b'Upload a Resume', blank=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='weblink_1',
            field=models.URLField(null=True, verbose_name=b'Weblink 1', blank=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='weblink_2',
            field=models.URLField(null=True, verbose_name=b'Weblink 2', blank=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='weblink_3',
            field=models.URLField(null=True, verbose_name=b'Weblink 3', blank=True),
        ),
    ]
