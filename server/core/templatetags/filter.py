from django import template

register = template.Library()

@register.filter(name='update_variable')
def update_variable(value, arg):
    """Allows to update existing variable in template"""
    return arg

@register.simple_tag
def define(val=None):
  return val