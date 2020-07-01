# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(blank=True, to='skills.Category', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2014, max_length=4, choices=[(1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('project_name', models.CharField(max_length=150, null=True, blank=True)),
                ('officially_credited', models.BooleanField(default=False)),
                ('credit', models.ForeignKey(to='skills.Credit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weblink_1', models.URLField(help_text=b'e.g. IMDB Page', null=True, blank=True)),
                ('weblink_2', models.URLField(help_text=b'e.g. Twitter Page', null=True, blank=True)),
                ('weblink_3', models.URLField(help_text=b'e.g. Facebook Page', null=True, blank=True)),
                ('resume', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('affiliations', models.IntegerField(default=0, choices=[(0, b'Affiliations'), (1, b'DGC Directors Guild of Canada'), (2, b'IATSE'), (3, b'ACTRA - Alliance of Cinema, Television and Radio Artists'), (4, b'WGC Writers Guild of Canada ')])),
                ('other', models.CharField(max_length=150, null=True, blank=True)),
                ('local_number', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='skillsaffiliations',
            name='user',
        ),
        migrations.DeleteModel(
            name='SkillsAffiliations',
        ),
    ]
