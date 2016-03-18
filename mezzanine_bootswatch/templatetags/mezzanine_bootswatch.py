# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.simple_tag
def current_theme():
    site = Site.objects.get_current()
    try:
        site.bootswatch_theme.refresh_from_db()
        return site.bootswatch_theme
    except ObjectDoesNotExist:
        return None
