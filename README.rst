=============================
mezzanine_bootswatch
=============================

.. image:: https://badge.fury.io/py/mezzanine_bootswatch.png
    :target: https://badge.fury.io/py/mezzanine_bootswatch

Bootswatch integration

Documentation
-------------

The full documentation is at https://mezzanine_bootswatch.readthedocs.org.

Quickstart
----------

Install mezzanine_bootswatch::

    pip install git+git://github.com/beetleman/mezzanine_bootswatch.git

Then use it in a project by add to settings.py::

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


Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

TODO
----

* tests

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
