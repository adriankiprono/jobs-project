# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-24 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0010_auto_20200123_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='last_name',
            new_name='company',
        ),
        migrations.AddField(
            model_name='applicant',
            name='contact',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
