# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181117_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/Users/macbook/Desktop/garlic-farm.jpg', upload_to='blog/static/images'),
        ),
    ]
