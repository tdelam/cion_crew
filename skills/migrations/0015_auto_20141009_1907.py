# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0014_auto_20141009_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='crew_position',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='creditoptions',
            name='credit',
        ),
        migrations.DeleteModel(
            name='Credit',
        ),
        migrations.AddField(
            model_name='creditoptions',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
