# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-23 09:25
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0005_auto_20200123_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='post',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
