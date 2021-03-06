# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-23 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_auto_20200122_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='avatar/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='image/'),
        ),
    ]
