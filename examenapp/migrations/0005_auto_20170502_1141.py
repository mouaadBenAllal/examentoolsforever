# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examenapp', '0004_auto_20170501_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fabriek',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='fabriek',
            name='updated_at',
        ),
    ]
