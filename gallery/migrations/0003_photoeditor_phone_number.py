# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180927_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoeditor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]