# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-18 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0010_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='title_list',
            field=models.ManyToManyField(related_name='title_list', to='tycoon.Title'),
        ),
        migrations.RemoveField(
            model_name='avatar',
            name='cur_title',
        ),
        migrations.AddField(
            model_name='avatar',
            name='cur_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cur_title', to='tycoon.Title'),
        ),
    ]
