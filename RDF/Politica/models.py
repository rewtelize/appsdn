# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Politica(models.Model):

    """
    .. class:: Politica

        Modelo de politica, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key=True, default=1)
    """Id del aplicacion"""

    politica = models.IntegerField(_('Politica'), null = False, unique=True)
    """Numero de la politica"""
    switch = models.CharField(_('Switch'), null = True, max_length=256)
    """Switch asociado a la politica"""
    origen = models.IntegerField(_('Puerto Origen'), null = True)
    """Puerto origen de la politica"""
    destino = models.IntegerField(_('Puerto Destino'), null = True)
    """Puerto destino de la politica"""
    accion = models.CharField(_('Accion'), null = True, max_length=256)
    """Accion a realizar sobre el paquete en la politica"""

class Politica_Usuario(models.Model):

    """
    .. class:: Politica_Usuario

        Modelo de politica, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key=True, default=1)
    """Id del aplicacion"""

    politica = models.IntegerField(_('Politica'), null = False)
    """Numero de la politica"""
    usuario = models.IntegerField(_('Usuario'), null = True)
    """Usuario referido en la politica"""