from django.conf.urls.defaults import patterns, url, include
from django_logtail.views import LogTailView, LogListView

urlpatterns = patterns('',
    url(
        r'^log/$',
        LogListView.as_view(),
        name='log_list'
    ),
    url(
        r'^log/(?P<logfile>[-\w\.]+)/$',
        LogTailView.as_view(),
        name='log_tail'
    ),
    url(
        r'^log/(?P<logfile>[-\w\.]+)/(?P<seek_to>\d+)/$',
        LogTailView.as_view(),
        name='log_seek'),
)
