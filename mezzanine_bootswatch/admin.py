from django.contrib import admin

from mezzanine_bootswatch.models import BootswatchTheme
from mezzanine_bootswatch.forms import BootswatchThemeForm


class BootswatchThemeAdmin(admin.ModelAdmin):
    form = BootswatchThemeForm
    list_display = ('name', 'site')

admin.site.register(BootswatchTheme, BootswatchThemeAdmin)
