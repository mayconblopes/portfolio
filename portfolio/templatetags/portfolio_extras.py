from django.template.defaultfilters import register


@register.filter
def get_first_tag(value):
    """
    Taking a String with tags (a lot of words separeted by ','), this function will retrun the first word
    get_first_tag('Mike, Nike, Dike') -> 'Mike'
    """
    return value[:value.find(',')]
