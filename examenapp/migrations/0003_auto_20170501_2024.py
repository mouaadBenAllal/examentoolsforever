# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 18:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenapp', '0002_auto_20170501_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabriek',
            name='telefoonnummer',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1234567891)]),
        ),
    ]
