# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0003_auto_20160803_2301'),
        ('tipo_usuario', '0002_auto_20160803_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
                ('id_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
                ('id_tipo_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_usuario.tipo_usuario')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'ordering': ('login',),
                'verbose_name': 'Usuario',
            },
        ),
    ]
