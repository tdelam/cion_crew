# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0018_skills_resident'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditoptions',
            old_name='officially_credited',
            new_name='imdb_credited',
        ),
    ]
