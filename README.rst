==============
django_logtail
==============

Introduction
============

Logtail allows you to view logfiles for your django project via your django
admin, and will also provide you with a live tail of the logfiles using ajax
polling - and therefore without the need for a long-running django process.

See Also: https://pypi.python.org/pypi/django_logtail

Installation and Use
====================

Django logtail takes a dictionary from your settings.py as follows::

    LOGTAIL_FILES = {
        'apache': '/var/www/www.foo.com.log',
        'django', '/var/log/www.foo.com/project.log',
    }

Add it via your installed apps::

    INSTALLED_APPS = (
        ...
        'django_logtail',
    )

If any of your django admin plugin apps already add a jquery header::

    LOGTAIL_INCLUDE_JQUERY = False # Default is True

Next hook it into your root_urlconf, above the bog-standard admin urls::

    urlpatterns = patterns('',
        # First this
        url(r'^admin/django_logtail/', include(logtail_urls)),

        # Then this
        url(r'^admin/', include(admin.site.urls)),
        ...
    )

Then absolutely ensure that the user that your django process runs as (whether
it's via wsgi, fastcgi, django runserver for debugging, or something else) has
permission to read all of the files in your LOGTAIL_FILES list.

logtail should then appear in your admin, and provide access to these files -
including a live tail of the file.

Simples.

Other Settings
==============

You can set the default update interval for the log tailing::

    LOGTAIL_UPDATE_INTERVAL = 50000 # Default is 1000 (one second)
