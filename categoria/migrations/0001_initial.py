# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0003_auto_20160803_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100)),
                ('id_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
            options={
                'ordering': ('categoria',),
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
    ]