from django import template
from django.conf import settings

url = settings.STATIC_URL

register = template.Library()

@register.simple_tag
def jquery():
    str = "<script type='text/javascript' src='{0}jquery-min.js' ></script> "

@register.simple_tag
def jquery_ui():
    str = "<script type='text/javascript' src='{0}jquery-ui.min.js' ></script> "
