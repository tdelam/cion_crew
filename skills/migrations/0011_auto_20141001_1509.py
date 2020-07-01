# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0010_auto_20140930_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='affiliations',
        ),
        migrations.AddField(
            model_name='skills',
            name='actra',
            field=models.BooleanField(default=False, verbose_name=b'ACTRA - Alliance of Cinema, Television and Radio Artists'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skills',
            name='dgc',
            field=models.BooleanField(default=False, verbose_name=b'DGC Directors Guild of Canada'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skills',
            name='iatse',
            field=models.BooleanField(default=False, verbose_name=b'IATSE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skills',
            name='wgc',
            field=models.BooleanField(default=False, verbose_name=b'WGC Writers Guild of Canada'),
            preserve_default=True,
        ),
    ]
