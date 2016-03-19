========
Usage
========

To use mezzanine_bootswatch in a project you need to add `mezzanine_bootswatch` in settings.py
It is recommended to place the `mezzanine_bootswatch` as high as possible, to make sure all the app templates are overridden.::
    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",
        "mezzanine_bootswatch",
        "mezzanine.boot",
        "mezzanine.conf",
        "mezzanine.core",
    ...
    )
