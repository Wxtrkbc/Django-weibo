# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(upload_to='UI/static/User_Pic'),
        ),
    ]
