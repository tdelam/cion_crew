# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_auto_20140930_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='weblink_1_description',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skills',
            name='weblink_2_description',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skills',
            name='weblink_3_description',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
    ]
