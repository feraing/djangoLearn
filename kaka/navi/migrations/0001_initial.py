# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('description', models.CharField(max_length=50, verbose_name='\u63cf\u8ff0')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
