# Generated by Django 3.0.2 on 2020-01-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('applicants', models.CharField(choices=[('EMPLOYER', 'employer'), ('EMPLOYEE', 'employee')], max_length=20)),
                ('jobs', models.CharField(max_length=50, null=True)),
                ('descriptions', models.TextField(max_length=200, null=True)),
                ('pay', models.PositiveIntegerField()),
            ],
        ),
    ]
