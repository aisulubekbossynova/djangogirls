# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181117_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/media/att.jpeg', upload_to=''),
        ),
    ]