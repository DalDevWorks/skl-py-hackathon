# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_scraper', '0015_auto_20170223_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitterUserName',
            field=models.CharField(default='No Handle Entered: 2017-02-23 19:20:01.122948', max_length=100, unique=True),
        ),
    ]