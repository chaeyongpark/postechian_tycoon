# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-10 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0002_auto_20170110_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(upload_to='images/avatar/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='icon',
            field=models.ImageField(upload_to='images/icon/'),
        ),
    ]
