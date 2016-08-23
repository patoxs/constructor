# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPresupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_presupuesto', models.CharField(max_length=200)),
                ('id_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
            options={
                'verbose_name': 'Tipo de presupuesto',
                'ordering': ('tipo_presupuesto',),
                'verbose_name_plural': 'Tipos de presupuesto',
            },
        ),
    ]
