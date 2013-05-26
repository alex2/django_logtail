from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_logtail import urls as logtail_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
