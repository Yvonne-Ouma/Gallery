# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=90)),
                ('category', models.ManyToManyField(to='gallery.Category')),
            ],
        ),
        migrations.AlterModelOptions(
            name='photoeditor',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='image',
            name='photoeditor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Photoeditor'),
        ),
    ]