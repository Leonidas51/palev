# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-22 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=100)),
                ('art_text', models.TextField()),
            ],
        ),
    ]
