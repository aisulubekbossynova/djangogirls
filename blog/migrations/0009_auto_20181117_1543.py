# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181117_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='MEDIA_ROOT+att.jpeg', upload_to=''),
        ),
    ]
