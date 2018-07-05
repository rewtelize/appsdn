# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Conmutador(models.Model):

    """
    .. class:: Conmutador

        Modelo de conmutador, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key=True, default=1)
    """Id del conmutador"""

    ip = models.CharField(_('Ip'), null = True, unique=True, max_length=128)
    """IP del conmutador"""
    nombre = models.CharField(_('Nombre'), null = True, max_length=128)
    """Nombre visible del conmutador"""
    version = models.CharField(_('Version'), max_length=256)
    """Version Openflow con la que esta trabajando el conmutador"""
    controlador = models.CharField(_('Controlador'), null = True, max_length=256)
    """IP del controlador al que esta conectado"""
    instancia = models.CharField(_('Instancia'), null = True, max_length=256)
    """Instancia asociada al conmutador"""
    fabricante = models.CharField(_('Fabricante'), null = True, max_length=256)
    """Fabricante del conmutador"""
