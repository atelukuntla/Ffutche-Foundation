# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributor_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=250)),
                ('contribution_type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
    ]