# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-10 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0003_auto_20170110_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='items',
            field=models.ManyToManyField(to='tycoon.Item'),
        ),
    ]
