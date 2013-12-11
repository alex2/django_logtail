==============
django_logtail
==============

Introduction
============

Logtail allows you to view logfiles for your django project via your django
admin, and will also provide you with a live tail of the logfiles using ajax
polling - and therefore without the need for a long-running django process.

Django 1.4+ compatible.

See Also: https://pypi.python.org/pypi/django_logtail

Installation and Use
====================

Django logtail takes a dictionary from your settings.py as follows::

    LOGTAIL_FILES = {
        'apache': '/var/www/www.foo.com.log',
        'django': '/var/log/www.foo.com/project.log',
    }

Add it via your installed apps::

    INSTALLED_APPS = (
        ...
        'django_logtail',
    )


Then absolutely ensure that the user that your django process runs as (whether
it's via wsgi, fastcgi, django runserver for debugging, or something else) has
permission to read all of the files in your LOGTAIL_FILES list.

logtail should then appear in your admin, and provide access to these files -
including a live tail of the file. Note that files will not appear if the
django process cannot access them.

Other Settings
==============

You can set the default update interval for the log tailing::

    LOGTAIL_UPDATE_INTERVAL = 50000 # Default is 3000 (three second)

Developing
==========

You can build a development environment using the following instructions::

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -e .
    python manage.py syncdb
    python manage.py runserver

Logtail ``dumpdata`` Issue
==========================

If you use ``python manage.py dumpdata``, be sure to add the
``--exclude=logtail`` flag to your command or you'll be presented with a::

    CommandError: Unable to serialize database: relation "django_logtail_log" does not exist
    LINE 1: SELECT "django_logtail_log"."id" FROM "django_logtail_log" O...

traceback when you run the dumpdata command. This is because django_logtail
needs to pretend that it has a model called ``Log`` when registering with the
django admin site (``ModelAdmin`` objects can't exist without being bound to a
``Model``).

``syncdb`` will still work however, because the pretend model is marked as
``managed = False``.
