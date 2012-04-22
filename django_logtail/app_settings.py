from django.conf import settings

LOGTAIL_FILES = getattr(settings, 'LOGTAIL_FILES', {})
LOGTAIL_INCLUDE_JQUERY = getattr(settings, 'LOGTAIL_INCLUDE_JQUERY', True)
