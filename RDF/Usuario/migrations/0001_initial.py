# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-30 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=128, null=True, unique=True, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=128, null=True, unique=True, verbose_name='Apellidos')),
                ('correo', models.CharField(max_length=256, verbose_name='Correo')),
                ('usuario', models.CharField(max_length=256, null=True, verbose_name='Usuario')),
                ('credencial', models.CharField(max_length=256, null=True, verbose_name='Contrase\xf1a')),
                ('es_admin', models.BooleanField(default=False, verbose_name='Alta')),
                ('ultima_sesion', models.DateTimeField()),
            ],
        ),
    ]