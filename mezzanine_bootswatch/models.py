from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class BootswatchTheme(models.Model):
    site = models.OneToOneField(Site, related_name='bootswatch_theme')
    name = models.CharField(max_length=200)
    url = models.CharField(_('Theme'), max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('theme')
        verbose_name_plural = _('themes')
