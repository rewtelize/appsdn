# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Aplicacion(models.Model):

    """
    .. class:: Aplicacion

        Modelo de aplicacion, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key=True, default=1)
    """Id del aplicacion"""

    nombre = models.CharField(_('Nombre'), null = True, unique=True, max_length=128)
    """Nombre visible de la aplicacion"""
    descripcion = models.CharField(_('Descripcion'), null = True, max_length=256)
    """Informacion sobre el comportamiento que imbuye"""
    archivo = models.CharField(_('Archivo'), null = True, max_length=256)
    """Nombre de la aplicacion"""
    fecha = models.DateTimeField()
    """Fecha de creacion"""
    autor = models.CharField(_('Autor'), null = True, max_length=256)
    """Persona u organizacion que ha creado el archivo"""