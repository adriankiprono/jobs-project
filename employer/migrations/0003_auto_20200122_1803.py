# Generated by Django 3.0.2 on 2020-01-22 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_auto_20200122_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='jobs',
            new_name='job',
        ),
    ]