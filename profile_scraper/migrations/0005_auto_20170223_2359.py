# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_scraper', '0004_auto_20170223_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitterUserName',
            field=models.CharField(default='No Handle Entered: 2017-02-23 23:59:18.935296', max_length=100, unique=True),
        ),
    ]