from django import template

register = template.Library()


@register.filter
def inc(value, arg):
    return int(value) + int(arg)


@register.simple_tag
def division(a, b, to_int=False):
    if to_int == True:
        return int(int(a) / int(b))
    else:
        return int(a) / int(b)
