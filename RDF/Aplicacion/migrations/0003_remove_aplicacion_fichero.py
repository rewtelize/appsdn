# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_aplicacion_fichero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aplicacion',
            name='fichero',
        ),
    ]
