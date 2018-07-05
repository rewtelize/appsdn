# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conmutador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conmutador',
            name='idps',
        ),
        migrations.AddField(
            model_name='conmutador',
            name='ip',
            field=models.CharField(max_length=128, null=True, unique=True, verbose_name='Ip'),
        ),
    ]
