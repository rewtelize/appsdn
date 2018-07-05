# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Grafico(models.Model):

    """
    .. class:: Grafico

        Modelo de grafico, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key=True, default=1)
    """Id del aplicacion"""

    fecha = models.DateTimeField()
    """Fecha de registro del trafico"""
    ip = models.CharField(_('Ip'), null = True, max_length=128)
    """Identificador del conmutador"""
    trafico = models.IntegerField(_('Trafico'), null = True)
    """MB generados con el trafico"""
    tipo = models.CharField(_('E/S'), null = True, max_length=256)
    """Trafico de entrada o salida"""
