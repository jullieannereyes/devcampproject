# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20171208_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(),
        ),
    ]
