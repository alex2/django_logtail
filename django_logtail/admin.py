from django.contrib import admin
from django_logtail.models import Log

class LogAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

admin.site.register(Log, LogAdmin)
