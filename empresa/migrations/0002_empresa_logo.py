# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]