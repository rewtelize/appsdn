# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grafico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafico',
            name='idps',
            field=models.CharField(max_length=128, null=True, verbose_name='Idps'),
        ),
    ]