# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='introduction',
            field=models.CharField(max_length=150),
        ),
    ]