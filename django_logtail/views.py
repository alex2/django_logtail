from os.path import getsize, isfile

from django_logtail import app_settings
from django.core import urlresolvers
from django.http import HttpResponse, Http404
from django.utils import simplejson as json
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django_logtail import app_settings

class HttpUnauthorized(HttpResponse):
    status_code = 401

class AdminLoginRequiredMixin(object):
    """Mixin to apply the login_required decorator to the as_view
    class method of a view.
    """
    @classmethod
    def as_view(cls, **initkwargs):
        return login_required(
            super(AdminLoginRequiredMixin, cls).as_view(**initkwargs),
        )

class UserCanViewLogsMixin(object):
    def dispatch(self, request, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            if not request.user.has_perm('django_logtail.can_view_logs'):
                return HttpUnauthorized('User does not have permission to view logs')
            return super(UserCanViewLogsMixin, self).dispatch(
                request, *args, **kwargs)

        return wrapper(request, *args, **kwargs)

class LogListView(UserCanViewLogsMixin, AdminLoginRequiredMixin, ListView):
    template_name = 'logtail/logtail_list.html'

    @property
    def queryset(self):
        for log, filename in app_settings.LOGTAIL_FILES.iteritems():
            if isfile(filename):
                yield (log, filename)


    def get_context_data(self, **kwargs):
        context = super(LogListView, self).get_context_data(**kwargs)
        context['include_jquery'] = app_settings.LOGTAIL_INCLUDE_JQUERY
        context['update_interval'] = app_settings.LOGTAIL_UPDATE_INTERVAL
        return context

class LogTailView(UserCanViewLogsMixin, AdminLoginRequiredMixin, View):
    """
    Returns JSON of the form::

        {
            "starts": "0",
            "data": "LOGFILEHERE"
            "ends": "3284",
        }
    """

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = {}
        seek_to = int(self.kwargs.get('seek_to', '0'))
        try:
            log_file_id = self.kwargs.get('logfile', '')
            log_file = app_settings.LOGTAIL_FILES[log_file_id]
        except KeyError:
            raise Http404('No such log file')

        try:
            file_length = getsize(log_file)
        except OSError:
            raise Http404('Cannot access file')

        if seek_to > file_length:
            seek_to = file_length

        try:
            context['log'] = file(log_file, 'r')
            context['log'].seek(seek_to)
            context['starts'] = seek_to
        except IOError:
            raise Http404('Cannot access file')

        return context

    def iter_json(self, context):
        yield '{"starts": "%d",' \
               '"data": "' % context['starts']

        while True:
            line = context['log'].readline()
            if line:
                yield json.dumps(line).strip(u'"')
            else:
                yield '", "ends": "%d"}' % context['log'].tell()
                context['log'].close()
                return

    def render_to_response(self, context):
        return HttpResponse(
            self.iter_json(context),
            content_type='application/json'
        )
