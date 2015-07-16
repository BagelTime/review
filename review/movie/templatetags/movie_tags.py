from django import template
from django.template.defaultfilters import stringfilter
from  django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
@stringfilter
def spoiler(value):
    p = re.compile('\*\*([^\*]+)\*\*')
    result = p.sub('<span class="spoiler" title="\\1">[SPOILER]</span>', value)
    return mark_safe(result)