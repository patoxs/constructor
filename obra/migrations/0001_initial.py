# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('mandante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_contrato', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('archivo', models.ImageField(blank=True, upload_to='')),
                ('id_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
                ('id_mandante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mandante.mandante')),
            ],
            options={
                'verbose_name': 'Obra',
                'ordering': ('nombre',),
                'verbose_name_plural': 'Obras',
            },
        ),
    ]
