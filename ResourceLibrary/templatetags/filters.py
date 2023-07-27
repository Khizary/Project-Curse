from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='getval')
def getval(value, key):
    """
        Returns the value turned into a list.
    """
    return value[key]

@register.filter(name='getidx')
def getidx(value, key):
    """
        Returns the value turned into a list.
    """
    return value.index(key)