from django import template
from django.conf import settings
import time

register = template.Library()

@register.simple_tag
def static_version(request):
    if settings.DEBUG:
        return {'STATIC_VERSION': str(int(time.time()))}
    return {'STATIC_VERSION': None}