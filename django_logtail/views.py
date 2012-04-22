from django_logtail import app_settings
from django.utils import simplejson as json
from django.views.generic import ListView
from django.views.generic.detail import BaseDetailView

class LogListView(ListView):
    template_name = 'logtail/logtail_list.html'
    queryset = app_settings.LOGTAIL_FILES

class LogTailView(BaseDetailView):
    def get_context_data(self, **kwargs):
        context = super(LogTailView, self).get_context_data(**kwargs)

    def render_to_response(self, context):
        return json.dumps(context['log'])
