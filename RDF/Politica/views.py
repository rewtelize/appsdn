# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import formContacto
from django.template.loader import render_to_string


