# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0021_skills_cpma'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='available_as',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
