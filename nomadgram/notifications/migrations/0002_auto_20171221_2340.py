# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-21 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
