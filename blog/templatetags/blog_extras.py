import markdown
from django import template

# register = template.Library()
from django.template.defaultfilters import register


@register.filter
def convert_markdown(value):
    return markdown.markdown(value)
