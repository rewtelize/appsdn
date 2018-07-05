# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Configuracion(models.Model):

    """
    .. class:: Configuracion

        Modelo de configuracion, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key= True, default=1, unique=True)
    """Id del configuracion"""

    nombre = models.CharField(_('Nombre'), null = True, unique=True, max_length=128)
    """Nombre visible del archivo"""
    nota = models.CharField(_('Nota'), null = True, max_length=256)
    """Informacion extra a tener en cuenta"""
    archivo = models.CharField(_('Archivo'), null = True, max_length=256)
    """Nombre del archivo de configuracion"""
    fecha = models.DateTimeField()
    """Fecha de creacion"""
