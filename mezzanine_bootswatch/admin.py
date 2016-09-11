from django.contrib import admin

from mezzanine_bootswatch.models import BootswatchTheme
from mezzanine_bootswatch.forms import BootswatchThemeForm


class BootswatchThemeAdmin(admin.ModelAdmin):
    form = BootswatchThemeForm
    list_display = ('name', 'site')

    class Media:
        css = {
            'all': ('mezzanine_bootswatch/css/admin.css',)
        }

admin.site.register(BootswatchTheme, BootswatchThemeAdmin)
