# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Usuario(models.Model):

    """
    .. class:: Usuario

        Modelo de usuario, hereda de la clase models.Model
    """

    id = models.AutoField(primary_key= True, default=1, unique=True)
    """Id del usuario"""

    nombre = models.CharField(_('Nombre'), null = True, unique=True, max_length=128)
    """Nombre del usuario"""
    apellidos = models.CharField(_('Apellidos'), null = True, unique=True, max_length=128)
    """Apellidos del usuario"""
    correo = models.CharField(_('Correo'), max_length=256)
    """Direccion email del usuario"""
    usuario = models.CharField(_('Usuario'), null = True, max_length=256)
    """Nombre de inicio de sesion"""
    credencial = models.CharField(_('Contraseña'), null = True, max_length=256)
    """Credencial para el inicio de sesion"""
    es_admin = models.BooleanField(_('Alta'), default=False)
    """Tomara valor verdad cuando sea administrador"""
    ultima_sesion = models.DateTimeField()
    """Fecha de la ultima sesion en el sistema"""
