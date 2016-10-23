============================
Changelog for django_logtail
============================

0.3.0 (2016-10-23)
------------------

- Add Django 1.10 and Python 3.5 compatibility (thanks @AlJohri)


0.2.0 (2013-12-11)
------------------

- Django 1.6 compatibility


0.1.1 (2013-05-26)
------------------

- Add the static folder to the MANIFEST.in


0.1.0 (2013-05-26)
------------------

- Adding ``django_logtail.urls`` to your project's ``ROOT_URLCONF`` is no
  longer necessary. All log tailing functionality has been moved to the
  ``ModelAdmin`` class in the form of the URLs and views.
- Now that the view is served from the ModelAdmin, use the Media class to define
  jquery dependency, and use django's built-in jquery object rather than using a
  CDN.
- Added example/ project for easier testing.
- Update documentation.


0.0.6 (2013-03-20)
------------------

- Use a CDN that does not serve gateway timeouts (mediatemple -> google)


0.0.5 (2013-03-20)
------------------

- Load the jquery js over https where required using a protocol-relative url.


0.0.4 (2012-12-20)
------------------

- Improved the quality of the javascript polling code
- The default poll time is now three seconds, rather than every one
- Now Django 1.3+ compatible (@victorgp)


0.0.3 (2012-08-16)
------------------

- Add the ability to turn off polling (@scott-w)


0.0.2 (2012-05-04)
------------------

- Escape log text to prevent html element lookalikes screwing up the formatting.


0.0.1 (2012-04-22)
------------------

- Update the package MANIFEST.in to ensure that the README and changelog are
  included.


0.0.0 (2012-04-22)
------------------

- Initial release.
