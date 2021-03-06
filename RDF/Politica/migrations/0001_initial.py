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
            name='Politica',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('politica', models.IntegerField(unique=True, verbose_name='Politica')),
                ('origen', models.IntegerField(null=True, verbose_name='Puerto Origen')),
                ('destino', models.IntegerField(null=True, verbose_name='Puerto Destino')),
                ('protocolo', models.CharField(max_length=256, null=True, verbose_name='Protocolo')),
                ('accion', models.CharField(max_length=256, null=True, verbose_name='Accion')),
            ],
        ),
        migrations.CreateModel(
            name='Politica_Usuario',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('politica', models.IntegerField(verbose_name='Politica')),
                ('usuario', models.IntegerField(null=True, verbose_name='Usuario')),
            ],
        ),
    ]
