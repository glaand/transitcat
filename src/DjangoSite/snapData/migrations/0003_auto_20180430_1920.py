# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapData', '0002_auto_20180430_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snappickle',
            name='pickleFileName',
            field=models.FilePathField(default=b''),
        ),
        migrations.AlterField(
            model_name='snappickle',
            name='snapFileName',
            field=models.FilePathField(default=b''),
        ),
    ]