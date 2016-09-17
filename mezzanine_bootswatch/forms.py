# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.core.cache import cache
from django import forms
from django.utils.safestring import mark_safe


from mezzanine_bootswatch.models import BootswatchTheme
from mezzanine_bootswatch import logger


BOOTSWATCH_API = "https://bootswatch.com/api/3.json"

CHOICE_TEMPLATE = """
<img src="{thumbnail}" alt={name}>
"""


class BootswatchThemeForm(forms.ModelForm):

    def __init__(self, *args, **kwsrgs):
        super(BootswatchThemeForm, self).__init__(*args, **kwsrgs)
        self.fields['url'] = forms.ChoiceField(
            choices=self.get_themes_choices(),
            widget=forms.RadioSelect
        )

    def get_themes(self):
        try:
            data = cache.get_or_set(
                'BOOTSWATCH_API_DATA',
                lambda: requests.get(BOOTSWATCH_API).json(),
                3600
            )
            return data['themes']
        except Exception as err:
            logger.exception(err)
            return []

    def get_theme_by_url(self, url):
        for t in self.get_themes():
            if t['cssCdn'] == url:
                return t
        return None

    def save(self, commit=True, *args, **kwargs):
        obj = super(BootswatchThemeForm, self).save(
            commit=False, *args, **kwargs
        )
        obj.name = self.get_theme_by_url(obj.url)['name']
        obj.save()
        return obj

    def get_theme_choice(self, theme):
        return mark_safe(CHOICE_TEMPLATE.format(**theme))

    def get_themes_choices(self):
        return [[theme['cssCdn'], self.get_theme_choice(theme)]
                for theme in self.get_themes()]

    class Meta:
        model = BootswatchTheme
        fields = ['site', 'url']
