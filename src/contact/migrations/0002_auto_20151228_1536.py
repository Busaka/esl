# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 15:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='school',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=datetime.datetime(2015, 12, 28, 15, 36, 36, 132126, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
    ]