# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_scraper', '0005_auto_20170223_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitterUserName',
            field=models.CharField(default='No Handle Entered: 2017-02-23 18:01:48.170525', max_length=100, unique=True),
        ),
    ]