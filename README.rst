==============
django_logtail
==============

Introduction
============

Logtail allows you to view logfiles for your django project via your django
admin, and will also provide you with a live tail of the logfiles using ajax
polling - and therefore without the need for a long-running django process.

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

Absolutely ensure that the user that your django process (whether it's wsgi,
fastcgi, django runserver for debugging, or something else) has permission to
read all of the files in your LOGTAIL_FILES list.

Then logtail will appear in your admin, and provide access to these files -
including a live tail of the file.

Simples.
